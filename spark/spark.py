#!/usr/bin/env python

#title           :spark.py
#description     :The current python file reads the data from s3 and runs job on top of it
#author		     :Ajay Krishna Teja Kavuri
#date            :02012017
#version         :0.1
#==============================================================================

# Libraries
from pyspark import SparkContext
import sys
import traceback
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

    # Method has sets the bucket name and file path
    def setS3Attrs(self,bucketName,filePath):
        # Set the attributes
        self.bucketName = bucketName
        self.filePath = filePath

    # Fetch data from s3 instead of manual text files
    def getDataS3(self):

        try:
            # build the query from S3
            s3Uri = "s3n://"+str(self.bucketName)+"/"+str(self.filePath)
            # Get the file from S3
            s3Data = self.sparkCntxt.textFile(s3Uri)

            return s3Data

        # Exception
        except Exception:
            traceback.print_exc()
            return False

    # Method that will implement the actual jobs
    def runJobWithCache(self,cacheData):
        # Simple filter for testing
        numOfAs = cacheData.filter(lambda s: 'a' in s).count()

        # Debug statements
        print "Number of A's:" + str(numOfAs)

    # Job for counting consumption
    def runJob(self,data):
        print data.count()

# main method
if __name__ == '__main__':

    # Get the arguments that you need
    bucketName = str(sys.argv[1])
    filePath = str(sys.argv[2])

    # Initialize the class
    thisSparkJob = Spark()

    # get the context
    sc = thisSparkJob.getContext()

    # Set s3 parameters
    thisSparkJob.setS3Attrs(bucketName,filePath)

    # get the data cache
    data = thisSparkJob.getDataS3()

    # run the job
    thisSparkJob.runJob(data)

    # stop the job
    sc.stop()
