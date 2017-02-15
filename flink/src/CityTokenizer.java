/**
 *title           :consumeFromKafka.java
 *description     :The java program is for reading the stream from kafka
 *author		  :Ajay Krishna Teja Kavuri
 *date            :01302017
 *version         :0.1
 *==============================================================================
 */

import org.apache.flink.api.common.functions.FlatMapFunction;
import org.apache.flink.api.java.tuple.Tuple3;
import org.apache.flink.util.Collector;

/**
 * Packages
 *==============================================================================
 */

public class CityTokenizer implements FlatMapFunction<String, Tuple3<Long, String, Double>> {

    // Mao funtion that can split the input string into tokens

    @Override
    public void flatMap(String rcrd, Collector<Tuple3<Long,String, Double>> collector) throws Exception {
        // Split the string into the values
        String[] tkns = rcrd.split(",",-1);

        // Debug statements
        //for (String tkn:tkns) {
        //    System.out.print(tkn+"\t");
        //}
        // System.out.print("Original record: "+rcrd);
        //System.out.print("Adding: "+tkns[0]+","+tkns[5]);

        // Append them to the collector
        collector.collect(new Tuple3<Long,String, Double>(Long.parseLong(tkns[6]),tkns[4],Double.parseDouble(tkns[5])));
    }
}
