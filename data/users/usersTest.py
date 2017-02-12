#!/usr/bin/env python

#title           :users_test.py
#description     :Class to test the users logic
#author		     :Ajay Krishna Teja Kavuri
#date            :01222017
#version         :0.1
#==============================================================================

# Libraries
import unittest
from users import UsersEngine
#==============================================================================

class UsersTest(unittest.TestCase):

    # Setup method
    def setUp(self):
        # Initiate class
        self.thisEngne =  UsersEngine(100,1)

    # Test for user data generation
    def testGenUsr(self):
        # execute method
        usrRow = self.thisEngne.genUsr()

        # get the length of the usr row
        self.assertEqual(len(usrRow), 5)

    # Test for user data generation
    def testGenCmpny(self):
        # execute method
        cmpnyRow = self.thisEngne.genCmpny()

        # get the length of the usr row
        self.assertEqual(len(cmpnyRow), 5)

# Main funtion
if __name__ == '__main__':
    # initite and run the unittest
    unittest.main()
