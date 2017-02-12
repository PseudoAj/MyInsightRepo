#!/usr/bin/env python

#title           :water.py
#description     :The script is for generating fake water meters data
#author		     :Ajay Krishna Teja Kavuri
#date            :02122017
#version         :0.1
#==============================================================================

# Libraries

import datetime
import random
import traceback
import csv
import sys
from kafka import KafkaProducer
from kafka.errors import KafkaError

#==============================================================================

# Implementation

class Water():

    # Initialize
    def __init__(self,address='default',duration=1):

        # Debug statement
        print "initialized"

# Main method
if __name__ == '__main__':

    # Read the arguments

    # Debug statement
    print 'Argument List:', str(sys.argv)

    # Initialize the class
    thisWtrProdcr =  Water(5,1)
