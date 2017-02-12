#!/bin/bash

#title           :stream_cluster_setup.sh
#description     :This script will install all the required packages for stream cluster
#author		       :Ajay Krishna Teja Kavuri
#date            :01212017
#version         :0.1
#==============================================================================
# Read the variables

## read the cluster name
clustername="de-ny-ajay-stream"

#==============================================================================
# Some housekeeping

## fetch
eval `ssh-agent -s`
peg fetch $clustername

## Update for no reason
peg sshcmd-cluster $clustername "sudo apt-get -y update"

## Install git
peg sshcmd-cluster $clustername "sudo apt-get -y install git"
#==============================================================================
# Install required stack for the stream cluster

## SSH
peg install $clustername ssh

## AWS
peg install $clustername aws

## Zookeeper
peg install $clustername zookeeper

## Kafka
peg install $clustername kafka

## Kafka manager
peg install $clustername kafka-manager

## Hadoop
peg install $clustername hadoop

## Flink
peg install $clustername flink

## redis
peg sshcmd-node $clustername 1 "sudo apt-get update && sudo apt-get install redis-server -y"
