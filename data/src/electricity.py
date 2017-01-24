#!/usr/bin/env python

#title           :electricity.py
#description     :The script is for generating fake electricity meters data
#author		     :Ajay Krishna Teja Kavuri
#date            :01222017
#version         :0.1
#==============================================================================

# Libraries

#==============================================================================

# Implementation

class Electricity():

    # Initialize
    def __init__(self,intrvl,duration,regFilePath,elecFilePath):

        # Define the intrvl
        self.intrvl = intrvl

        # Define the duration
        self.duration = duration

        # Set the file path for the registrations
        self.regDataFilePath = regFilePath

        # Set the file to write the elecrticity data
        self.elecFilePath = elecFilePath

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

        # Debug statement
        # print "#====================#"
        # print "Electricity initialized with "+str(self.intrvl)+" interval, "+str(self.duration)+" duration and filepath of "+str(self.regDataFilePath)

    # Method to generate the data
    def generate(self):

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
            print len(self.regDataDict)
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
