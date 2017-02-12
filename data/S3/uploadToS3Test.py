#!/usr/bin/env python

#title           :uploadToS3Test.py
#description     :This class will test the upload logic to s3 bucket
#author		     :Ajay Krishna Teja Kavuri
#date            :02122017
#version         :0.1
#==============================================================================

# Libraries
import datetime
import random
import traceback
import time
import csv
from kafka import KafkaProducer
from kafka.errors import KafkaError
#==============================================================================
