#!/usr/bin/env python

#title           :electricityTest.py
#description     :Class to test the electricity logic
#author		     :Ajay Krishna Teja Kavuri
#date            :02122017
#version         :0.1
#==============================================================================

# Libraries
import unittest
from electricity import Electricity
#==============================================================================

class ElectricityTest(unittest.TestCase):

    # Setup method
    def setUp(self):
        # Initiate class
        self.thisElec =  Electricity()

    # Test for the list to csv
    def testReadAll(self):

        # check for the right execution
        self.assertTrue(self.thisElec.readAll())


# Main funtion
if __name__ == '__main__':
    # initite and run the unittest
    unittest.main()
