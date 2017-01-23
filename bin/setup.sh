#!/bin/bash

#title           :setup.sh
#description     :This script will install all the required packages for me
#author		       :Ajay Krishna Teja Kavuri
#date            :01212017
#version         :0.1
#==============================================================================

# Ritual to update the files for no reson
sudo apt-get update

# Install python and all the required packages
pip install Faker
