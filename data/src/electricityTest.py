#!/usr/bin/env python

#title           :electricityTest.py
#description     :Class to test the electricity logic
#author		     :Ajay Krishna Teja Kavuri
#date            :01222017
#version         :0.1
#==============================================================================

# Libraries
import unittest
from electricity import Electricity
#==============================================================================

class UsersTest(unittest.TestCase):

    # Setup method
    def setUp(self):
        # Initiate class
        self.thisElec =  Electricity()

    # Test for the list to csv
    def testConvrtLstToCSV(self):
        # Define a list
        testList = ["a","b","c"]

        # Pass the list
        testCSV = self.thisElec.convrtLstToCSV(testList)

        # check for the right execution
        self.assertEqual(testCSV, "a,b,c")

# Main funtion
if __name__ == '__main__':
    # initite and run the unittest
    unittest.main()
