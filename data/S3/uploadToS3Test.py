#!/usr/bin/env python

#title           :uploadToS3Test.py
#description     :This class will test the upload logic to s3 bucket
#author		     :Ajay Krishna Teja Kavuri
#date            :02122017
#version         :0.1
#==============================================================================

# Libraries
import unittest
from uploadToS3 import S3
#==============================================================================

class S3Test(unittest.TestCase):

    # Setup method
    def setUp(self):
        # define a bucket name
        bcktNme = "de-ny-ajay"

        # Initiate class
        self.thisS3 = S3(bcktNme)

    # Test for the list to csv
    def testCheckBucket(self):

        # check for the null string
        self.assertTrue(self.thisS3.checkBucket())



# Main funtion
if __name__ == '__main__':
    # initite and run the unittest
    unittest.main()
