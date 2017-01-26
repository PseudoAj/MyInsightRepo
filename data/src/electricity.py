#!/usr/bin/env python

#title           :electricity.py
#description     :The script is for generating fake electricity meters data
#author		     :Ajay Krishna Teja Kavuri
#date            :01222017
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
    def __init__(self,intrvl,duration,regFilePath,elecFilePath,cnctnAddr='default'):

        # Define the intrvl
        self.intrvl = datetime.timedelta(seconds=int(intrvl))

        # Define step size
        self.step = datetime.timedelta(seconds=1)

        # Define the duration
        self.duration = datetime.timedelta(days=int(duration))

        # Set the file path for the registrations
        self.regDataFilePath = regFilePath

        # Set the file to write the elecrticity data
        self.elecFilePath = elecFilePath

        # define a header to work with
        self.elecHeaderData = ['service_id', 'user_name','type','reg_time','state','consumption','end_time']

        # set the start date
        self.elctStrtTime = datetime.datetime(2017, 01, 01, 00, 00, 00)

        # calculate the end time
        self.elctEndTime = self.elctStrtTime + self.duration

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

        # check if the address is defaulted
        if cnctnAddr != 'default':

            # Initialize the address
            self.cnctnAddr = cnctnAddr

            # Initialize the class
            self.producer = KafkaProducer(bootstrap_servers=self.cnctnAddr)

            # define the topic you want to send
            self.topic = 'electricity'


        # Debug statement
        # print "#====================#"
        # print "Electricity initialized with "+str(self.intrvl)+" interval, "+str(self.duration)+" duration and filepath of "+str(self.regDataFilePath)

    # Method to generate the data
    def generate(self):

        # write the header first
        self.writeFile(self.elecFilePath,self.elecHeaderData)

        # first generate a hashmaps
        self.genHashMaps()

        # simulate events
        # Assume current time is start time
        curTime = self.elctStrtTime

        # Run through the loop
        while curTime < self.elctEndTime:

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
                    curRcrdRow = self.genElecRow(curRcrdDict,int(curStrTime),int(newTimeStmp))

                    # write into the file
                    self.writeFile(self.elecFilePath,curRcrdRow)


                # Debug statement
                # print str(curSrvceId) +","+ str(curRcrdDict)
                # raw_input()

                # update the next time stamp by pop and insert
                # print self.timeDataDict.get(int(curStrTime))
                self.timeDataDict[int(newTimeStmp)] = self.timeDataDict.get(int(curStrTime))
                self.timeDataDict.pop(int(curStrTime))

            # increment curTime
            curTime+=self.step

            # Debug statement
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



    # Method to generate the hashmaps
    def genHashMaps(self):
        # Put everything into one dict
        # Read the user data file
        with open(self.regDataFilePath) as regDataFile:
            # Ignore the header
            regDataFile.readline()

            # For each registration
            for reg in regDataFile:
                # dict for current record
                curRcrdDict = {}

                # call for the method
                service_id, user_name, type, strtTime, state = self.getTokens(reg)

                # Assgn then to the dict
                curRcrdDict['service_id']=service_id
                curRcrdDict['user_name']=user_name
                curRcrdDict['type']=type
                curRcrdDict['strtTime']=strtTime
                curRcrdDict['state']=state

                # Add the records into another dictionary
                self.regDataDict[str(service_id)] = curRcrdDict

                # append them with the service key
                if not int(strtTime) in self.timeDataDict:
                    # Create a new entry and add value
                    self.timeDataDict[int(strtTime)]=[str(service_id)]
                else:
                    # Append to the list
                    self.timeDataDict.get(int(strtTime)).append(str(service_id))

                # Debug statement
                # print self.timeDataDict
                # raw_input()
                # print "Current service id: "+str(service_id)+",start time: "+str(strtTime)+",username: "+str(user_name)+",type: "+str(type)

            # Debug statement
            # print len(self.regDataDict)
            # print self.regDataDict
            # raw_input()
            # print "Current service id: "+str(service_id)+",start time: "+str(strtTime)+",username: "+str(user_name)+",type: "+str(type)

    # Method to strip and split the tokns
    def getTokens(self,rcrd):

        # Get the record and split for tokens
        rcrdValList = rcrd.split(',')

        # Assign them to the corressponding tokens
        service_id = rcrdValList[0]
        user_name = rcrdValList[1]
        type = rcrdValList[2]
        strtTime = rcrdValList[3]
        state = rcrdValList[4]

        # Debug statement
        # print "Current service id: "+str(service_id)+",start time: "+str(strtTime)+",username: "+str(user_name)+",type: "+str(type)
        # raw_input()

        # Return the values
        return service_id, user_name, type, strtTime, state

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
            self.produceStream(data)

            # Debug statement
            # print "#====================#"
            # print "Data written to csv: "+str(data)

            # Return a cute true
            return True

        # Exception
        except Exception:
            traceback.print_exc()
            return False

    # Method to write the data into kafka
    def produceStream(self,curData):

        # Send data continously
        while True:

            # send the data
            self.producer.send(self.topic, curData[0])
