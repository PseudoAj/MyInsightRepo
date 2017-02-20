#!/bin/bash

#title           :peg.sh
#description     :This script will install all the required packages for stream cluster
#author		       :Ajay Krishna Teja Kavuri
#date            :01212017
#version         :0.1
#==============================================================================
# Read the variables

## read the cluster name
clustername="de-ny-ajay-batch"

#==============================================================================
# Some housekeeping

## fetch
eval `ssh-agent -s`
peg fetch $clustername

## SSH
peg install $clustername ssh

## AWS
peg install $clustername aws

## Update for no reason
peg sshcmd-cluster $clustername "sudo apt-get -y update"

## Install git
peg sshcmd-cluster $clustername "sudo apt-get -y install git"
#==============================================================================
# Install required stack for the stream cluster

## Hadoop
peg install $clustername hadoop

## spark
peg install $clustername spark

## cassandra
peg sshcmd-node $clustername 1 "sudo apt-get -y install mysql-server libmysqlclient-dev"
