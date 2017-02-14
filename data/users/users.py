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
import uuid
import traceback
import subprocess
import radar
import datetime
import pickle
#==============================================================================
class UsersEngine():

    # Initialization
    def __init__(self,numOfRegs,duration):

        # Debug statement
        # print "Initialization"

        # Assign the number of registrations to create
        self.numOfRegs = numOfRegs

        # Define the duration in seconds for data generation
        self.duration = datetime.timedelta(seconds=duration)

        # Assign a percentile of business
        self.bizPrcnt = 6

        # Assign the percentile of users and business
        self.numOfBizs = int(self.bizPrcnt*self.numOfRegs/100)
        self.numOfUsrs = self.numOfRegs-self.numOfBizs

        # Define the time for generating batch
        self.btchEndTime = datetime.datetime.now()

        # Calculate the start time
        self.btchStrtTime = self.btchEndTime - self.duration

        # Initialize faker for generating fake data
        self.faker = Faker()

        # Header for the file
        self.regHeaderData = ['service_id', 'user_name','type','reg_time','state','zipcode']

        # Define a list of states
        self.states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
                       "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                       "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                       "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                       "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

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

        # put all registrations into one dict
        # structure:
        # {service_id:
        #   {
        #       service_id: record_val
        #               .
        #               .
        #               .
        #   }
        # }
        self.regDataDict = {}

        # put all the data for the time in one dict
        self.timeDataDict = {}

        # put the metadata in one dict
        self.regMetaDataDict = {}

        # Assign required values values to meta
        self.regMetaDataDict['strtTime'] = self.btchStrtTime
        self.regMetaDataDict['numOfRegs'] = self.numOfRegs

        # Clear some files before attempting to write
        self.cleanFiles()


    # Method to delete the files that have been previously written
    def cleanFiles(self):
        # Registration
        # Define the command
        thisCmd = 'rm -rf '+str(self.regDataFilePath)
        # Run the command
        self.runBash(thisCmd)

        # Start time dictionaries
        # Define the command
        thisCmd = 'rm -rf '+str(self.timeDictFilePath)
        # Run the command
        self.runBash(thisCmd)

        # Meta Data file
        # Define the command
        thisCmd = 'rm -rf '+str(self.metaDataFilePath)
        # Run the command
        self.runBash(thisCmd)

    # simple function to run the bash command
    def runBash(self,cmd):
        # Run a cmd and return exceptions if any
        try:
            subprocess.call(cmd,shell=True)
        except Exception:
            traceback.print_exc()

    # Method to create one user
    def genUsr(self):

        # Variables
        curRow = {}

        # use faker to get the required attribute
        srvceId = self.getUniqId()
        usrNme = self.faker.name()
        type = 'household'
        # Generate a random starting time
        regTime = radar.random_datetime(start=self.btchStrtTime, stop=self.btchEndTime)
        regTime = regTime.strftime("%s")
        state = str(choice(self.states))

        # compact them into one list
        curRow['service_id'] = srvceId
        curRow['user_name'] = usrNme.replace(",", "")
        curRow['type'] = type
        curRow['strtTime'] = regTime
        curRow['state'] = state

        # debug statement
        # print "#====================#"
        # print "Current user details: "+str(usrNme)

        # Return statement
        return curRow

    # Method to generate company profile
    def genCmpny(self):

        # Variables
        curRow = {}

        # use faker to generate the company info
        srvceId = self.getUniqId()
        cmpnyNme = str(self.faker.company())
        type = 'business'
        # Generate a random starting time
        regTime = radar.random_datetime(start=self.btchStrtTime, stop=self.btchEndTime)
        regTime = regTime.strftime("%s")
        state = str(choice(self.states))

        # compact them into one list
        curRow['service_id'] = srvceId
        curRow['user_name'] = cmpnyNme.replace(",", "")
        curRow['type'] = type
        curRow['strtTime'] = regTime
        curRow['state'] = state

        # debug statement
        # print "#====================#"
        # print "Current company details: "+str(cmpnyNme)

        # Return statement
        return curRow

    # Method to generate an unique ID
    def getUniqId(self):

        # Use uuid4 and return an unique id
        return str(uuid.uuid4())

    # Define a method just to generate the registrations
    def genRegistrations(self):

        # Write the header before generating any data
        # self.self.writeFile(self.regDataFilePath,self.regHeaderData)

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
                    curRcrdDict = self.genUsr()
                    #self.writeFile(self.regDataFilePath,self.genUsr())
                    usrCnt+=1
                # otherwise just write the biz info
                else:
                    curRcrdDict = self.genCmpny()
                    #self.writeFile(self.regDataFilePath,self.genCmpny())
                    bizCnt+=1
            # Vice-versa
            elif curType == 1:
                # check for the count of users exceeding ratio
                if bizCnt < self.numOfBizs:
                    # write user data
                    curRcrdDict = self.genCmpny()
                    #self.writeFile(self.regDataFilePath,self.genCmpny())
                    bizCnt+=1
                # otherwise just write the biz info
                else:
                    curRcrdDict = self.genUsr()
                    #self.writeFile(self.regDataFilePath,self.genUsr())
                    usrCnt+=1

            # Add the row to the dict
            # Get the necessary values
            curRcrdSrvceId = curRcrdDict.get('service_id')
            curRcrdStrtTime = curRcrdDict.get('strtTime')
            self.regDataDict[str(curRcrdSrvceId)] = curRcrdDict

            # Add row to time dict
            # append them with the service key
            if not int(curRcrdStrtTime) in self.timeDataDict:
                # Create a new entry and add value
                self.timeDataDict[int(curRcrdStrtTime)]=[str(curRcrdSrvceId)]
            else:
                # Append to the list
                self.timeDataDict.get(int(curRcrdStrtTime)).append(str(curRcrdSrvceId))

        # Debug statement
        print "#====================#"
        print "Generated "+str(usrCnt)+" users, "+str(bizCnt)+" business registrations"

    # Method to save the dictionary to pickle format
    def saveToPckl(self,path,dict):
        # Try writing the file
        try:
            # open and write the data list
            with open(path,'wb') as pckleObj:
                # write down the data passed on to it
                pickle.dump(dict,pckleObj)

            # Return a cute true
            return True

        # Exception
        except Exception:
            traceback.print_exc()
            return False

    # Method to save generate pickle files for dicts
    def saveAll(self):

        # Save the dictionary
        self.saveToPckl(self.regDataFilePath,self.regDataDict)
        self.saveToPckl(self.timeDictFilePath,self.timeDataDict)
        self.saveToPckl(self.metaDataFilePath,self.regMetaDataDict)

# The main method to trigger the execution
if __name__ == '__main__':

    # Define the required variables
    # Inputs from users
    ## Number of users in the system
    print "#====================#"
    print "Enter number of registrations(ex: 500 users/businesses):"
    numOfRegs = int(raw_input())
    # duration for the batch/stream in minutes
    print "#====================#"
    print "Enter duration for generating data(ex: 60 days):"
    duration = int(raw_input())

    # create object for triggering execution
    ## Initialize the main class and run through
    thisEngne =  UsersEngine(numOfRegs,duration)

    # Start the user generation logic
    thisEngne.genRegistrations()

    # Save them into pickle for further processing
    thisEngne.saveAll()
