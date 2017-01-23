#!/usr/bin/env python

#title           :main.py
#description     :The class will trigger events
#author		     :Ajay Krishna Teja Kavuri
#date            :01222017
#version         :0.1
#==============================================================================

# Libraries
from faker import *
from random import *
import uuid
import traceback
import subprocess
import csv
#==============================================================================

# Implementation

class DataEngine():

    # Initialization
    def __init__(self,numOfRegs,intrvl,duration):

        # Assign the number of registrations to create
        self.numOfRegs = numOfRegs

        # Assign the interval for the sensors
        self.intrvl = intrvl

        # Define the duration for data generation
        self.duration = duration

        # Assign a percentile of business
        self.bizPrcnt = 6

        # Assign the percentile of users and business
        self.numOfBizs = int(self.bizPrcnt*self.numOfRegs/100)
        self.numOfUsrs = self.numOfRegs-self.numOfBizs

        # Initialize the faker class for generating data
        self.faker = Faker()

        # Define the header for the file
        self.regHeaderData = ['service_id', 'user_name','type','zipcode']

        # Set the directory to save the users dat
        self.regDataDir = "../output/registrations/"

        # Set the name for user data file
        self.regDataFileName = "reg.dat"

        # create the path for registration data file
        self.regDataFilePath = self.regDataDir+self.regDataFileName

        # Clear some files before attempting to write
        self.cleanFiles()

        # Debug statement
        # print "#====================#"
        # print "Method initialized with "+str(self.numOfUsrs)+" users, "+str(self.numOfBizs)+" business and interval of "+str(self.intrvl)

    # Method to trigger the data
    # Creates the users and then uses the users to generate the utility info
    def generate(self):

        # Write the header before generating any data
        self.writeFile(self.regDataFilePath,self.regHeaderData)

        # Variables for the counters
        usrCnt = 0
        bizCnt = 0

        # generate users and business details for the number of users
        for i in xrange(self.numOfRegs):

            # Introduce randomness
            curType = randint(0,1)

            # Check for the type
            # 0: users
            # 1: Business
            if curType == 0:
                # check for the count of users exceeding ratio
                if usrCnt < self.numOfUsrs:
                    # write user data
                    self.writeFile(self.regDataFilePath,self.genUsr())
                    usrCnt+=1
                # otherwise just write the biz info
                else:
                    self.writeFile(self.regDataFilePath,self.genCmpny())
                    bizCnt+=1
            # Vice-versa
            elif curType == 1:
                # check for the count of users exceeding ratio
                if bizCnt < self.numOfBizs:
                    # write user data
                    self.writeFile(self.regDataFilePath,self.genCmpny())
                    bizCnt+=1
                # otherwise just write the biz info
                else:
                    self.writeFile(self.regDataFilePath,self.genUsr())
                    usrCnt+=1

    # Method to create one user
    def genUsr(self):

        # Variables
        curRow = []

        # use faker to get the required attribute
        srvceId = self.getUniqId()
        usrNme = self.faker.name()
        type = 'household'
        srvceZipCode = self.faker.zipcode()

        # compact them into one list
        curRow.append(srvceId)
        curRow.append(usrNme)
        curRow.append(type)
        curRow.append(srvceZipCode)

        # debug statement
        # print "#====================#"
        # print "Current user details: "+str(usrNme)

        # Return statement
        return curRow

    # Method to generate company profile
    def genCmpny(self):

        # Variables
        curRow = []

        # use faker to generate the company info
        srvceId = self.getUniqId()
        cmpnyNme = self.faker.company()
        type = 'business'
        srvceZipCode = self.faker.zipcode()

        # compact them into one list
        curRow.append(srvceId)
        curRow.append(cmpnyNme)
        curRow.append(type)
        curRow.append(srvceZipCode)

        # debug statement
        # print "#====================#"
        # print "Current company details: "+str(cmpnyNme)

        # Return statement
        return curRow

    # Method to generate an unique ID
    def getUniqId(self):

        # Use uuid4 and return an unique id
        return str(uuid.uuid4())

    # Method to write the data to a certain file
    def writeFile(self, filePath, data):
        # Try writing the file
        try:
            # open and write the data list
            with open(filePath,'a+') as curFile:
                # write down the data passed on to it
                curFileWrtr = csv.writer(curFile)
                curFileWrtr.writerow(data)

            # Debug statement
            # print "#====================#"
            # print "Data written to csv: "+str(data)

            # Return a cute true
            return True

        # Exception
        except Exception:
            traceback.print_exc()
            return False

    # Method to delete the files that have been previously written
    def cleanFiles(self):
        # Define the command
        thisCmd = 'rm -rf '+str(self.regDataFilePath)
        # Run the command
        self.runBash(thisCmd)

    # simple function to run the bash command
    def runBash(self,cmd):
        # Run a cmd and return exceptions if any
        try:
            subprocess.call(cmd,shell=True)
        except Exception:
            traceback.print_exc()

if __name__ == '__main__':

    # Define the variables
    # Number of registrations
    numOfRegs = 100
    # Interval for the stream
    intrvl = 5
    # duration for the batch/stream in minutes
    duration = 60

    # Initialize the main class and run through
    thisEngne =  DataEngine(numOfRegs,intrvl,duration)

    # Triger the data generation
    thisEngne.generate()
