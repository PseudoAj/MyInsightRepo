#!/usr/bin/env python

#title           :comsumeMsgs.py
#description     :The class is a simple cosumer to print message
#author		     :Ajay Krishna Teja Kavuri
#date            :01252017
#version         :0.1
#==============================================================================

# Libraries

from kafka import KafkaConsumer
#==============================================================================

# Implementation

class Consumer():

    # Initialize
    def __init__(self, cnctnAddr):

        # Assign the connection
        self.cnctnAddr = cnctnAddr

        # Have a group id to optimize the consumer
        self.grpId = 'test-consumer'

        # Assign a topic
        self.topic = 'electricity'

        # Initialize the consumer here
        self.consumer = KafkaConsumer(self.topic, group_id=self.grpId, bootstrap_servers=self.cnctnAddr)

    # Actual method to start consuming
    def consumeMsgs(self):

        # Loop through the consumer
        for message in self.consumer:

            # Print the consumer
            print "Message topic: "+str(message.topic)+" Message partition: "+str(message.partition)+" Message offset: "+str(message.offset)+" Message key: "+str(message.key)+" Message value: "+str(message.value)

# Main method for triggering consumptiom
if __name__ == '__main__':

    # Define the address
    cnctnAddr = '172.31.0.234:9092'

    # Initialize the class
    thisConsumer = Consumer(cnctnAddr)

    # start the consumer
    thisConsumer.consumeMsgs()
