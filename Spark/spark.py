#!/usr/bin/env python

#title           :spark.py
#description     :The current python file reads the data from s3 and runs job on top of it
#author		     :Ajay Krishna Teja Kavuri
#date            :02012017
#version         :0.1
#==============================================================================

# Libraries
from pyspark import SparkContext
#==============================================================================

# Implementation

class Spark():

    # Initialize
    def __init__(self,clusterURL = "local",appName = "AUTH"):
        # Define the file location
        self.source = "/home/ubuntu/MyInsightRepo/README.md"

        # Define the cluster url
        self.clusterURL = clusterURL

        # Define the app name
        self.appName = appName

        # Debug statement
        print "Initialized"

    # Method to call for spark context
    def getContext(self):
        # get back the spark context
        self.sparkCntxt = SparkContext(self.clusterURL,self.appName)

        return self.sparkCntxt


    # Method would return the source context for spark
    def getDataCache(self):
        # pass the source with context
        cacheData = self.sparkCntxt.textFile(self.source).cache()

        return cacheData

    # Method that will implement the actual jobs
    def runJobWithCache(self,cacheData):
        # Simple filter for testing
        numOfAs = cacheData.filter(lambda s: 'a' in s).count()

        # Debug statements
        print numOfAs


# main method
if __name__ == '__main__':

    # Get the arguments that you need

    # Initialize the class
    thisSparkJob = Spark()

    # get the context
    sc = thisSparkJob.getContext()

    # get the data cache
    cache = thisSparkJob.getDataCache()

    # run the job
    thisSparkJob.runJobWithCache(cache)

    # stop the job
    sc.stop()
