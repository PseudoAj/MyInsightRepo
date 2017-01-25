#!/usr/bin/env python

#title           :producer.py
#description     :The class is a simple producer and Implementation of https://github.com/InsightDataScience/data-engineering-ecosystem/wiki/Kafka-advanced#create-a-kafka-producer-on-your-local-machine
#author		     :Ajay Krishna Teja Kavuri
#date            :01252017
#version         :0.1
#==============================================================================

# Libraries
import random
import sys
import six
from datetime import datetime
from kafka.client import SimpleClient
from kafka.producer import KeyedProducer
#==============================================================================

# Main class for defining the producer
class Producer(object):

    # Initialization for the class with address
    def __init__(self, addr):

        self.client = SimpleClient(addr)
        self.producer = KeyedProducer(self.client)
        self.topic = 'test_ajay_topic'

    # Main method for simulation
    def produce_msgs(self, source_symbol):

        # Generate some random data
        price_field = random.randint(800,1400)
        # Count the messages in the tunnel
        msg_cnt = 0

        # Loop for the feilds
        while True:

            # Get a random time value
            time_field = datetime.now().strftime("%Y%m%d %H%M%S")
            # Get a random price value
            price_field += random.randint(-10, 10)/10.0
            # Get a random volume feild
            volume_field = random.randint(1, 1000)

            # Format your string
            str_fmt = "{};{};{};{}"

            # Create the message
            message_info = str_fmt.format(source_symbol,
                                          time_field,
                                          price_field,
                                          volume_field)

            # Print for debug
            print message_info

            # Send the message
            self.producer.send_messages(self.topic, source_symbol, message_info)

            # Messages count
            msg_cnt += 1

# Main method for triggering the producers
if __name__ == "__main__":

    # Get the arguments
    args = sys.argv
    ip_addr = str(args[1])
    partition_key = str(args[2])

    # Initiate a class
    prod = Producer(ip_addr)
    # Trigger the producer method
    prod.produce_msgs(partition_key)
