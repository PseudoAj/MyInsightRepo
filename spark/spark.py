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
from operator import add
import traceback
import MySQLdb
import os
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

        # create a connection to database
        self.mysqlConn = MySQLdb.connect(host="localhost",user="root",passwd=str(os.environ["AUTH_MYSQL_PASS"]),db="auth")

        # cursor for running sql
        self.mysqlCursor = self.mysqlConn.cursor()

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

        try:
            # Simple filter for testing
            numOfAs = cacheData.filter(lambda s: 'a' in s).count()

            # Debug statements
            print "Number of A's:" + str(numOfAs)

        # Exception
        except Exception:
            traceback.print_exc()
            return False

    # Job for counting consumption
    def runJob(self,data):

        try:
            # Run the job, key by user_id and add the consumption
            cnsmptnByUser = data.flatMap(lambda x:x.split('\n'))\
                                .map(lambda x:(str(x.split(',')[0]),float(x.split(',')[5])))\
                                .reduceByKey(add)

            # Collect the results
            output = cnsmptnByUser.collect()

            return output

        # Exception
        except Exception:
            traceback.print_exc()
            return False

    # Insert the values into db
    def insertToDB(self,data):

        # Run through the data and buid a query for each record and execute
        for user_id, consmptn  in data:
            sqlStatment = "INSERT INTO `consumption` (`user_id`,`updated_time`,`con_elec`) VALUES ('"+str(user_id)+"','"+str(self.filePath).replace(".dat","").split("/",1)[1]+"','"+str(consmptn)+"')"

            try:
                exMsg = self.mysqlCursor.execute(sqlStatment)

            except Exception:
                self.mysqlConn.rollback()
                traceback.print_exc()

        # Commit after all transactions
        print self.mysqlConn.commit()


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
    output = thisSparkJob.runJob(data)

    # Insert the computed data into mysql
    thisSparkJob.insertToDB(output)

    thisSparkJob.mysqlConn.close()

    # stop the job
    sc.stop()
