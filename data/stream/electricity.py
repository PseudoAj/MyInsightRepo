#!/usr/bin/env python

#title           :electricity.py
#description     :The script is for generating fake electricity meters data
#author		     :Ajay Krishna Teja Kavuri
#date            :02032017
#version         :0.1
#==============================================================================

# Libraries

import datetime
import random
import traceback
import csv
from kafka import KafkaProducer
from kafka.errors import KafkaError

#==============================================================================

# Implementation

class Electricity():

    # Initialize
    def __init__(self,intrvl,duration):

        # Debug statement
        print "initialized"

# Main method
if __name__ == '__main__':

    # Get the variables from the arguments
