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
import sys
import pickle
from kafka import KafkaProducer
from kafka.errors import KafkaError

#==============================================================================

# Implementation

class Electricity():

    # Initialize
    def __init__(self,duration=1,intrvl=5,cnctnAddr='default'):
        # Define the directory to output
        self.regDataDir = "../output/registrations/"

        # Set the name for user data file
        self.regDataFileName = "users"

        # Set the name for the time dict file
        self.timeDictFileName = "time"

        # Set the name for start time dict file
        self.metaDataFileName = "meta"

        # create the path for files
        self.regDataFilePath = self.regDataDir+self.regDataFileName
        self.timeDictFilePath = self.regDataDir+self.timeDictFileName
        self.metaDataFilePath = self.regDataDir+self.metaDataFileName

        # Read the pickle files
        self.readAll()

        # Get the start time for the data generation
        self.strtTime = self.metaDataDict.get('strtTime')

        # Get the number of users
        self.numOfRegs = self.metaDataDict.get('numOfRegs')

        # Debug statement
        # print "Starting time: "+str(self.strtTime)+" Number of registrations: "+str(self.numOfRegs)

    # method to read all the files
    def readAll(self):
        # Try writing the file
        try:
            # Read all the pickle files into dict
            self.regDataDict = self.readFromPickle(self.regDataFilePath)
            self.timeDataDict = self.readFromPickle(self.timeDictFilePath)
            self.metaDataDict = self.readFromPickle(self.metaDataFilePath)

            # Return statement
            return True

        # Exception
        except Exception:
            traceback.print_exc()
            return False


    # method to pickle files for user generated data
    def readFromPickle(self,path):
        # Try writing the file
        try:
            # open and write the data list
            with open(path,'rb') as pckleObj:
                # write down the data passed on to it
                dict = pickle.load(pckleObj)

            # Return a cute true
            return dict

        # Exception
        except Exception:
            traceback.print_exc()
            return False

    # simple function to run the bash command
    def runBash(self,cmd):
        # Run a cmd and return exceptions if any
        try:
            subprocess.call(cmd,shell=True)
        except Exception:
            traceback.print_exc()


# Main method
if __name__ == '__main__':

    # Read the arguments

    # Debug statement
    print 'Argument List:', str(sys.argv)

    # Initialize the class
    thisElcProdcr =  Electricity()
