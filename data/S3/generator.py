s#!/usr/bin/env python

#title           :electricity.py
#description     :The script is for generating fake electricity meters data
#author		     :Ajay Krishna Teja Kavuri
#date            :02032017
#version         :0.1
#==============================================================================

# Libraries

from uploadToS3 import S3
import datetime
import random
import traceback
import csv
import time
import sys
import pickle
import subprocess
#==============================================================================

# Implementation

class Generator():

    # Initialize
    def __init__(self,duration=1,intrvl=5,topic="electricity"):

        # Define the intrvl
        self.intrvl = datetime.timedelta(seconds=int(intrvl))

        # Define step size
        self.step = datetime.timedelta(seconds=1)

        # Define the duration
        self.duration = datetime.timedelta(days=int(duration))

        # define the topic you want to send
        self.topic = str(topic)

        # Define the durectory for temporary data
        self.tmpDir = "./tmp/"

        # Define the name for tmp file
        self.tmpFileName = self.topic+".dat"

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
        self.tmpDataFilePath = self.tmpDir+self.tmpFileName

        # Read the pickle files and clean temo files
        self.readAll()
        self.cleanTempFiles()

        # Get the start time for the data generation
        self.strtTime = self.metaDataDict.get('strtTime')

        # Get the number of users
        self.numOfRegs = self.metaDataDict.get('numOfRegs')

        # Get the end time
        self.endTime = self.strtTime + self.duration

        # Define the bucket name
        self.bcktNme = "de-ny-ajay"

        # S3 Initialize
        self.thisS3 = S3(self.bcktNme)

        # Debug statement
        # print "Starting time: "+str(self.strtTime)+" End time: "+str(self.endTime)+" Number of registrations: "+str(self.numOfRegs)

    # Clean the temporary files
    def cleanTempFiles(self):
        # run the bash command to clean it
        # clean the tmp file
        # temp file
        # Define the command
        thisCmd = 'rm -rf '+str(self.tmpDataFilePath)
        # Run the command
        self.runBash(thisCmd)


    # simple function to run the bash command
    def runBash(self,cmd):
        # Run a cmd and return exceptions if any
        try:
            subprocess.call(cmd,shell=True)
        except Exception:
            traceback.print_exc()


    # method to read all the files
    def readAll(self):
        # Try writing the file
        try:
            # Read all the pickle files into dict
            self.regDataDict = self.readFromPickle(self.regDataFilePath)
            self.timeDataDict = self.readFromPickle(self.timeDictFilePath)
            self.metaDataDict = self.readFromPickle(self.metaDataFilePath)

            # Debug statement
            print str(self.topic)+": Completed reading files."

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

    # Method to start the producer
    def produce(self):

        # Get the current time
        curTime = self.strtTime

        # Get instance for next day
        nextDay = self.strtTime + datetime.timedelta(days=1)

        # Run through for the time
        while curTime < self.endTime:

            # check if the curTime exceeded one day
            if curTime >= nextDay:
                # upload to s3
                self.thisS3.upload(self.topic,self.tmpDir,self.tmpFileName,str(curTime)+".dat")

                # Clean the temp files after upload
                self.cleanTempFiles()

                # Debug statement
                print "Start time: "+str(self.strtTime)+", now time: "+str(curTime)

                # update
                nextDay += datetime.timedelta(days=1)

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

                # for all the service id write the record
                for curSrvceId in curSrvceList:
                    # Get the dictionary
                    curRcrdDict = self.regDataDict.get(str(curSrvceId))

                    # pass on the dict to wite the csv file
                    curRcrdRow = self.genRow(curRcrdDict,int(curStrTime),int(newTimeStmp))

                    # send the data in producers
                    # Append them as a csv row
                    curRcrdRowStr = self.convrtLstToCSV(curRcrdRow)

                    # send them through the producer
                    self.writeFile(self.tmpDataFilePath,curRcrdRowStr)

                    # # Debug statement
                    # print curRcrdRowStr

                    # # Debug statement
                    #print "Writing: "+str(curSrvceId)+" at time: "+str(curStrTime)
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

            # Debug statement
            # print remngTime
            # print "Current time: "+str(curStrTime)+" ,next timestamp: "+str(newTimeStmp)+" dict: "+str(self.timeDataDict)
            # raw_input()

    # Function for reading the dictionary and generating a consumption rate
    def genRow(self,rcrdDict,startTime,endTime):

        # variable to store the row
        curRcrd = []

        # determine the consumptionrate
        if self.topic == "gas":
            cnsmptnRate = 0.00045
        elif self.topic == "water":
            cnsmptnRate = 0.023
        else:
            cnsmptnRate = 0.30

        # get all the attributes
        service_id = rcrdDict.get('service_id')
        user_name = rcrdDict.get('user_name')
        type = rcrdDict.get('type')
        strtTime = rcrdDict.get('strtTime')
        state = rcrdDict.get('state')
        consumption = float(random.triangular(0,float(cnsmptnRate)))

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

    # function to convert given list of strings and integers to a csv line
    def convrtLstToCSV(self, lst):

        # covert each part as string
        for idx,rcrd in enumerate(lst):
            lst[idx] = str(rcrd)

        # return with join
        return ",".join(lst)

    # Method to write the data to a certain file
    def writeFile(self, filePath, data):
        # Try writing the file
        try:
            # open and write the data list
            with open(filePath,'a+') as curFile:
                # write down the data passed on to it
                curFileWrtr = csv.writer(curFile)
                curFileWrtr.writerow(data)

            # also write it on the producer
            # self.produceStream(data)

            # Debug statement
            # print "#====================#"
            # print "Data written to csv: "+str(data)

            # Return a cute true
            return True

        # Exception
        except Exception:
            traceback.print_exc()
            return False

# Main method
if __name__ == '__main__':

    # Get the arguments
    ## duration
    dur = int(sys.argv[1])
    ## Interval
    intrvl = int(sys.argv[2])
    ## topic
    topic = str(sys.argv[3])

    # Initialize the class
    thisGenrtr =  Generator(dur,intrvl,topic)

    # Start the producer method
    thisGenrtr.produce()
