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

    # Simple test case
    def testPass(self):
        # assertion statement
        self.assertTrue(True)

# Main funtion
if __name__ == '__main__':
    # initite and run the unittest
    unittest.main()
