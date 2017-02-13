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
import time
import sys
import pickle
from kafka import KafkaProducer
from kafka.errors import KafkaError

#==============================================================================

# Implementation

class Electricity():

    # Initialize
    def __init__(self,duration=1,intrvl=5,cnctnAddr='default'):

        # Define address
        self.cnctnAddr = cnctnAddr

        # Define the intrvl
        self.intrvl = datetime.timedelta(seconds=int(intrvl))

        # Define step size
        self.step = datetime.timedelta(seconds=1)

        # Define the duration
        self.duration = datetime.timedelta(days=int(duration))

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

        # Get the end time
        self.endTime = self.strtTime+self.duration

        # Initialize the class
        self.producer = KafkaProducer(bootstrap_servers=self.cnctnAddr)

        # define the topic you want to send
        self.topic = 'electricity'

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

    # Method to start the producer
    def produce(self):

        # Get the current time
        curTime = self.strtTime

        # Run through for the time
        while curTime < self.endTime:

            # Get the loop start time
            loopStrtTime = datetime.datetime.now()

            # Convert the current time into a unix time stamp
            curStrTime = curTime.strftime("%s")

            # New time stamp
            newTime = curTime + self.intrvl
            newTimeStmp = newTime.strftime("%s")

            # check if it exists in the time dict
            if int(curStrTime) in self.timeDataDict:

                # write a value for this data
                # get the service_id
                curSrvceList = self.timeDataDict.get(int(curStrTime))

                # Debug statement
                print len(curSrvceList)

                # for all the service id write the record
                for curSrvceId in curSrvceList:
                    # Get the dictionary
                    curRcrdDict = self.regDataDict.get(str(curSrvceId))

                    # pass on the dict to wite the csv file
                    curRcrdRow = self.genElecRow(curRcrdDict,int(curStrTime),int(newTimeStmp))

                    # send the data in producers
                    # Append them as a csv row
                    curRcrdRowStr = self.convrtLstToCSV(curRcrdRow)

                    # send them through the producer
                    self.produceStream(curSrvceId, curRcrdRowStr)

                    # # Debug statement
                    # print curRcrdRowStr

                    # # Debug statement
                    # print "Writing: "+str(curSrvceId)+" at time: "+str(curStrTime)
                    # raw_input()

                # update the next time stamp by pop and insert
                # print self.timeDataDict.get(int(curStrTime))
                # Check if the timestamp already exists
                if int(newTimeStmp) in self.timeDataDict:
                    # Append to existing list
                    self.timeDataDict[int(newTimeStmp)] = self.timeDataDict.get(int(newTimeStmp))+self.timeDataDict.get(int(curStrTime))
                else:
                    # Else just create a new list
                    self.timeDataDict[int(newTimeStmp)] = self.timeDataDict.get(int(curStrTime))
                # remove the element
                self.timeDataDict.pop(int(curStrTime))

            # increment curTime
            curTime+=self.step

            # Get the time for loop end
            loopEndTime = datetime.datetime.now() - loopStrtTime
            loopEndTime = loopEndTime.total_seconds()
            remngTime = float(1-loopEndTime)

            # Sleep for that amount of time
            if remngTime>0:
                time.sleep(remngTime)

            # Debug statement
            # print remngTime
            # print "Current time: "+str(curStrTime)+" ,next timestamp: "+str(newTimeStmp)+" dict: "+str(self.timeDataDict)
            # raw_input()

    # Function for reading the dictionary and generating a consumption rate
    def genElecRow(self,rcrdDict,startTime,endTime):

        # variable to store the row
        curRcrd = []

        # get all the attributes
        service_id = rcrdDict.get('service_id')
        user_name = rcrdDict.get('user_name')
        type = rcrdDict.get('type')
        strtTime = rcrdDict.get('strtTime')
        state = rcrdDict.get('state')
        consumption = float(random.triangular(0,0.30))

        # append the attributes to one list
        curRcrd.append(service_id)
        curRcrd.append(user_name)
        curRcrd.append(type)
        curRcrd.append(startTime)
        curRcrd.append(state)
        curRcrd.append(consumption)
        curRcrd.append(endTime)

        # return the list
        return curRcrd

    # Method to write the data into kafka
    def produceStream(self,curKey,curData):

        # send the data
        self.producer.send(self.topic, key=str(curKey), value=curData)

    # function to convert given list of strings and integers to a csv line
    def convrtLstToCSV(self, lst):

        # covert each part as string
        for idx,rcrd in enumerate(lst):
            lst[idx] = str(rcrd)

        # return with join
        return ",".join(lst)

# Main method
if __name__ == '__main__':

    # Read the arguments

    # Debug statement
    print 'Argument List:', str(sys.argv)

    # Get the arguments
    ## duration
    dur = int(sys.argv[1])
    ## Interval
    intrvl = int(sys.argv[2])
    ## Producer address
    addr = sys.argv[3]


    # Initialize the class
    thisElcProdcr =  Electricity(dur,intrvl,addr)

    # Start the producer method
    thisElcProdcr.produce()
