import org.apache.flink.api.java.tuple.Tuple3;
import org.apache.flink.streaming.api.TimeCharacteristic;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.functions.source.RichParallelSourceFunction;
import org.apache.flink.streaming.api.windowing.assigners.TumblingTimeWindows;
import org.apache.flink.streaming.api.windowing.time.Time;

import java.util.Random;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class streamExample {

    public static void main(String[] args) throws Exception {

        final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        env.setStreamTimeCharacteristic(TimeCharacteristic.IngestionTime);

        // create a stream of sensor readings, assign timestamps
        DataStream<Tuple3<Double, Long, String>> readings = env
                .addSource(new SimpleDataGenerator());

        readings
                .keyBy(2)
                .window(TumblingTimeWindows.of(Time.seconds(1)))
                .sum(0)
                .writeAsCsv("out");

        env.execute("Ingestion time example");

    }

    /* class used to generate a stream of data.
     in many practical problems this is not needed, as your source will likely be from
     a queueing systems like Kafka or Kinesis
    */
    static class SimpleDataGenerator extends RichParallelSourceFunction<Tuple3<Double, Long, String>> {

        private static final int numSensors = 1000;
        private volatile boolean running = true;

        @Override
        public void run(final SourceContext<Tuple3<Double, Long, String>> ctx) throws Exception {
            final ScheduledExecutorService exec = Executors.newScheduledThreadPool(2);
            final Random rnd = new Random();
            try {
                while (running) {

                    // create a variably delayed event from all sensors
                    for (int i = 0; i < numSensors; i++) {
                        long cur = System.currentTimeMillis();
                        Double reading = rnd.nextDouble();
                        String id = Integer.toString(i);
                        final Tuple3<Double, Long, String> event = new Tuple3(reading, cur, id);

                        exec.schedule(() -> {
                            ctx.collect(event);
                        }, 600, TimeUnit.MILLISECONDS);
                    }
                    Thread.sleep(500);
                }
            } finally {
                exec.shutdownNow();
            }
        }

        @Override
        public void cancel() {
            running = false;
        }
    }
}