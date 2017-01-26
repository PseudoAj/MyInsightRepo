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
    def __init__(self):

        # Debug statement
        print "Initialization"

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
    print "Enter duration for system(ex: 60 days):"
    duration = int(raw_input())


    # create object for triggering execution
