#!/usr/bin/env python

#title           :producer.py
#description     :The class is a simple producer and Implementation of https://github.com/InsightDataScience/data-engineering-ecosystem/wiki/Kafka-advanced#create-a-kafka-producer-on-your-local-machine
#author		     :Ajay Krishna Teja Kavuri
#date            :01252017
#version         :0.1
#==============================================================================

# Libraries

from kafka import KafkaProducer
from kafka.errors import KafkaError
#==============================================================================

# Implementation

class Producer():

    # Initialize
    def __init__(self, cnctnAddr):

        # Define the connection
        self.cnctnAddr = cnctnAddr

        # Initialize a new producer
        self.producer = KafkaProducer(bootstrap_servers=self.cnctnAddr)

        # define the toic you want to send
        self.topic = 'electricity'

        # count the messages sent
        self.prdceCnt = 0

    # Method to produce messages
    def produceMsgs(self):

        # Generate some data
        curData = 'test data'

        # Send data continously
        while True:

            # send the data
            self.producer.send(self.topic, bcurData)
            # Increament
            self.prdceCnt += 1

# Main method to call for the class
if __name__ == '__main__':

    # Define the address
    cnctnAddr = '172.31.0.232:9092'

    # initialize the class
    thisProducer = Producer(cnctnAddr)

    # start the producer
    thisProducer.produceMsgs()
