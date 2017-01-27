#!/usr/bin/env python

#title           :users.py
#description     :The class will generate users for it to use it for streaming
#author		     :Ajay Krishna Teja Kavuri
#date            :01222017
#version         :0.1
#==============================================================================

# Libraries
from faker import *
from random import *
import sys
import uuid
import traceback
import subprocess
import radar
import datetime
import csv
#==============================================================================

# Implementation
class UsersEngine():

    # Initialization
    def __init__(self,numOfRegs,intrvl,duration):

        # Debug statement
        print "Initialization"

        # Assign the number of registrations to create
        self.numOfRegs = numOfRegs

        # Assign the interval in days for the sensors
        self.intrvl = intrvl

        # Define the duration in seconds for data generation
        self.duration = datetime.timedelta(secs=500)

        # Assign a percentile of business
        self.bizPrcnt = 6

        # Assign the percentile of users and business
        self.numOfBizs = int(self.bizPrcnt*self.numOfRegs/100)
        self.numOfUsrs = self.numOfRegs-self.numOfBizs

        # Define the time for generating batch
        self.btchEndTime = datetime.datetime.now()


# The main method to trigger the execution
if __name__ == '__main__':

    # Define the required variables

    # Inputs from users
    ## Number of users in the system
    print "#====================#"
    print "Enter number of registrations(ex: 500 users/businesses):"
    numOfRegs = int(raw_input())
    # Interval for the stream
    print "#====================#"
    print "Enter interval for system(ex: 5 seconds):"
    intrvl = int(raw_input())
    # duration for the batch/stream in minutes
    print "#====================#"
    print "Enter duration for system(ex: 60 senconds):"
    duration = int(raw_input())

    # create object for triggering execution
    ## Initialize the main class and run through
    thisEngne =  UsersEngine(numOfRegs,intrvl,duration)
