/**
 *title           :RedisExampleMapper.java
 *description     :The java program is for adding a sink to flink
 *author		  :Ajay Krishna Teja Kavuri
 *date            :02032017
 *version         :0.1
 *==============================================================================

 */

/**
 * Packages
 *==============================================================================
 */

import org.apache.flink.api.java.tuple.Tuple3;
import org.apache.flink.streaming.connectors.redis.common.mapper.RedisCommand;
import org.apache.flink.streaming.connectors.redis.common.mapper.RedisCommandDescription;
import org.apache.flink.streaming.connectors.redis.common.mapper.RedisMapper;

/**
 * Imlementation
 *==============================================================================
 */

public class RedisTopicMapper implements RedisMapper<Tuple3<Long, String, Double>> {

    // Define a topic variable
    private String topic;

    // Constructor
    public RedisTopicMapper(String topic) {
        this.topic = topic;
    }

    // Assign a hash  name
    @Override
    public RedisCommandDescription getCommandDescription(){
        // Assign a hash name for the command

        return new RedisCommandDescription(RedisCommand.LPUSH,"real_time");
    }

    // Assign a key
    @Override
    public String getKeyFromData(Tuple3<Long, String, Double> data){
        return data.f1+":"+this.topic;
    }

    // Assign a value
    @Override
    public String getValueFromData(Tuple3<Long, String, Double> data){
        return Double.toString(data.f2);
    }
}
