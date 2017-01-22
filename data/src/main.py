#!/usr/bin/env python

#title           :main.py
#description     :The class will trigger events
#author		     :Ajay Krishna Teja Kavuri
#date            :01222017
#version         :0.1
#==============================================================================

# Libraries
from faker import Faker

#==============================================================================

# Implementation

class DataEngine():

    # Initialization
    def __init__(self,numOfUsrs,intrvl):

        # Assign the number of users to create
        self.numOfUsrs = numOfUsrs

        # Assign the interval for the sensors
        self.intrvl = intrvl

        # Initialize the faker class for generating data
        self.faker = Faker()

        # Debug statement
        print "#====================#"
        print "Method initialized with "+str(self.numOfUsrs)+" users and interval of "+str(self.intrvl)

    # Method to trigger the data
    # Creates the users and then uses the users to generate the utility info
    def generate(self):

        # generate user details for the number of users
        for i in xrange(self.numOfUsrs):
            self.genUsr()
            self.genCmpny()

    # Method to create one user
    def genUsr(self):

        # use faker to get the required attribute
        usrNme = self.faker.name()

        # debug statement
        print "#====================#"
        print "Current user details: "+str(usrNme)

    # Method to generate company profile
    def genCmpny(self):

        # use faker to generate the company info
        cmpnyNme = self.faker.company()

        # debug statement
        print "#====================#"
        print "Current company details: "+str(cmpnyNme)

if __name__ == '__main__':

    # Define the variables
    numOfUsrs = 50
    intrvl = 5

    # Initialize the main class and run through
    thisEngne =  DataEngine(numOfUsrs,intrvl)

    # Triger the data generation
    thisEngne.generate()
