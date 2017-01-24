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
import sys
import uuid
import traceback
import subprocess
import radar
import datetime
import csv
import electricity
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

        # Define the time for batch
        self.btchStrtTime = '2017-01-1T00:00:00'
        self.btchEndTime = '2017-01-03T23:59:59'

        # Initialize the faker class for generating data
        self.faker = Faker()

        # Define the header for the file
        self.regHeaderData = ['service_id', 'user_name','type','reg_time','state','zipcode']

        # Define a list of states
        self.states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA","HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

        # Set the directory to save the users dat
        self.regDataDir = "../output/registrations/"

        # Set the directory to save the utility dat
        self.utilityDataDir = "../output/utility/"

        # Set the name for electricity data file
        self.elecDataFileName = "electricity.dat"

        # Set the name for user data file
        self.regDataFileName = "reg.dat"

        # create the path for registration data file
        self.regDataFilePath = self.regDataDir+self.regDataFileName

        # create the path for electricity data file
        self.elecDataFilePath = self.utilityDataDir+self.elecDataFileName

        # Initialize the electricity class
        self.electricity = electricity.Electricity(self.intrvl,self.duration,self.regDataFilePath,self.elecDataFilePath)

        # Clear some files before attempting to write
        self.cleanFiles()

        # Debug statement
        # print "#====================#"
        # print "Method initialized with "+str(self.numOfUsrs)+" users, "+str(self.numOfBizs)+" business and interval of "+str(self.intrvl)

    # Define a method just to generate the registrations
    def genRegistrations(self):

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

        # Debug statement
        print "#====================#"
        print "Generated "+str(usrCnt)+" users, "+str(bizCnt)+" business registrations"


    # Method to trigger the data
    # Creates the users and then uses the users to generate the utility info
    def generate(self):

        # Trigger the registrations first
        self.genRegistrations()

        # Similarly trigger the electricity
        self.electricity.generate()

    # Method to create one user
    def genUsr(self):

        # Variables
        curRow = []

        # use faker to get the required attribute
        srvceId = self.getUniqId()
        usrNme = self.faker.name()
        type = 'household'
        # Generate a random starting time
        regTime = radar.random_datetime(start=self.btchStrtTime, stop=self.btchEndTime)
        regTime = regTime.strftime("%s")
        state = str(choice(self.states))
        srvceZipCode = self.faker.zipcode()

        # compact them into one list
        curRow.append(srvceId)
        curRow.append(usrNme.replace(",", ""))
        curRow.append(type)
        curRow.append(regTime)
        curRow.append(state)
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
        cmpnyNme = str(self.faker.company())
        type = 'business'
        # Generate a random starting time
        regTime = radar.random_datetime(start='2017-01-1T00:00:00', stop='2017-01-03T23:59:59')
        regTime = regTime.strftime("%s")
        state = str(choice(self.states))
        srvceZipCode = self.faker.zipcode()

        # compact them into one list
        curRow.append(srvceId)
        curRow.append(cmpnyNme.replace(",", ""))
        curRow.append(type)
        curRow.append(regTime)
        curRow.append(state)
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
        # Registration
        # Define the command
        thisCmd = 'rm -rf '+str(self.regDataFilePath)
        # Run the command
        self.runBash(thisCmd)

        # Utility
        # Define the command
        thisCmd = 'rm -rf '+str(self.elecDataFilePath)
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
    print "#====================#"
    print "Enter number of registrations(ex: 500):"
    numOfRegs = int(raw_input())
    # Interval for the stream
    print "#====================#"
    print "Enter interval for system(ex: 5):"
    intrvl = int(raw_input())
    # duration for the batch/stream in minutes
    print "#====================#"
    print "Enter duration for system(ex: 60):"
    duration = int(raw_input())

    # Initialize the main class and run through
    thisEngne =  DataEngine(numOfRegs,intrvl,duration)

    # Triger the data generation
    thisEngne.generate()
