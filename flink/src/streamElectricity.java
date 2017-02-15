/**
 *title           :consumeFromKafka.java
 *description     :The java program is for reading the stream from kafka
 *author		  :Ajay Krishna Teja Kavuri
 *date            :02032017
 *version         :0.1
 *==============================================================================
 */

/**
 * Packages
 *==============================================================================
 */

import org.apache.flink.api.common.functions.MapFunction;
import org.apache.flink.streaming.api.TimeCharacteristic;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.functions.timestamps.AscendingTimestampExtractor;
import org.apache.flink.streaming.api.windowing.time.Time;
import org.apache.flink.api.java.tuple.Tuple3;
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer09;
import org.apache.flink.streaming.connectors.redis.RedisSink;
import org.apache.flink.streaming.connectors.redis.common.config.FlinkJedisPoolConfig;
import org.apache.flink.streaming.util.serialization.SimpleStringSchema;
import java.util.Properties;

public class streamElectricity {
    // Main Method
    public static void main(String[] args) throws Exception{

        // Variables for the kafka
        // Topic to read from
        String topic = args[0].toString();
        String consmrName = "flinkConsumer";

        // Redis configuration
        FlinkJedisPoolConfig redisConf = new FlinkJedisPoolConfig.Builder().setHost("172.31.0.231")
                .setPort(6379)
                .setPassword("hodor hodor hodor!!")
                .setTimeout(1000)
                .build();

        // Setup an execution environment
        StreamExecutionEnvironment envrnmnt = StreamExecutionEnvironment.getExecutionEnvironment();
        // Add time characterstic
        envrnmnt.setStreamTimeCharacteristic(TimeCharacteristic.EventTime);
        // Assign parllelism
        envrnmnt.setParallelism(1);

        // Define the properties for the connection
        Properties properties = new Properties();
        properties.setProperty("bootstrap.servers", "localhost:9092");
        properties.setProperty("group.id",consmrName);

        // Define the data stream
        DataStream<String> kafkaStream = envrnmnt.addSource(new FlinkKafkaConsumer09<String>(
                topic,new SimpleStringSchema(),properties
        ));

        // Rebalance before going further
        kafkaStream.rebalance();

        // Apply transformation
        DataStream<Tuple3<Long,String,Double>> electricityMap = kafkaStream.flatMap(new Tokenizer());

        // Add time characterstic
        DataStream syncElecStream = electricityMap.assignTimestampsAndWatermarks(new AscendingTimestampExtractor<Tuple3<Long, String, Double>>() {
            @Override
            public long extractAscendingTimestamp(Tuple3<Long, String, Double> electricityTuple) {
                // Return the time in format
                return electricityTuple.f0*1000;
            }
        });

        // Apply transformation
        DataStream sumOfConsumptn = syncElecStream.keyBy(1)
                .timeWindow(Time.minutes(1))
                .sum(2);


        // Add a sink to dump the processed values
        //sumOfConsumptn.writeAsCsv("consumptn");

        // Function to debug
        // sumOfConsumptn.print();

        // Sink to the redis
        sumOfConsumptn.addSink(new RedisSink<Tuple3<Long, String, Double>>(redisConf, new RedisTopicMapper(topic)));

        // Map for city analytics
        DataStream<Tuple3<Long,String,Double>> cityConsumptnMap = kafkaStream.flatMap(new CityTokenizer());

        // Add time characterstic
        DataStream syncCityElecStream = cityConsumptnMap.assignTimestampsAndWatermarks(new AscendingTimestampExtractor<Tuple3<Long, String, Double>>() {
            @Override
            public long extractAscendingTimestamp(Tuple3<Long, String, Double> electricityTuple) {
                // Return the time in format
                return electricityTuple.f0*1000;
            }
        });

        // Data stream for calculating consumption
        DataStream sumOfCityConsumptn = syncCityElecStream.keyBy(1)
                .timeWindow(Time.minutes(1))
                .sum(2);

        // Function to debug
        // sumOfCityConsumptn.print();

        // Sink to the redis
        sumOfCityConsumptn.addSink(new RedisSink<Tuple3<Long, String, Double>>(redisConf, new RedisTopicMapper(topic)));

        // Execute the function
        envrnmnt.execute("Processing for usage over last minute");
    }
}
