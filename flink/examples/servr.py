#!/usr/bin/env python

#title           :servr.py
#description     :The class will send some data to the server
#author		     :Ajay Krishna Teja Kavuri
#date            :01312017
#version         :0.1
#==============================================================================

# Libraries
import socket
import traceback
#==============================================================================

# Implementation

class Server():

    # Initialization
    def __init__(self,address,port):

        # Define the localhost and port
        self.address = address
        self.port = port

        # Debug statement
        print "Trying to connect to "+str(self.address)+":"+str(self.port)

    # Method to bind the server
    def bind(self):

        # Try to bind to the function
        try:

            # Initialize a socket
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # bind function
            self.socket.bind(self.address,self.port)
            
        # print the stack trace for exceptions
        except Exception:

            traceback.print_exc()

# main method to trigger the class
if __name__ == '__main__':

    # Define the key variables
    address = "localhost"
    port = "5005"

    # Initialize the class
    thisSrvr = Server(address,port)

    # Bind the server
    thisSrvr.bind()
