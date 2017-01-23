#!/bin/bash

#title           :peg.sh
#description     :This script will install all the required packages for me
#author		       :Ajay Krishna Teja Kavuri
#date            :01212017
#version         :0.1
#==============================================================================

# Read the variables

## pegasus path
read -p "Please enter pegasus path (Ex: /home/pseudoaj/GitHubRepos/pegasus): " pegdir
pegdir=${pegdir}

## read the tag name
read -p "Please enter your cluster name (Ex: de-ny-ajay): " clustername
clustername=${clustername}

#==============================================================================

# 1. Initialize

## change the path into pegasus directory
cd $pegdir

## Check if the directory has master and workers
if [ ! -f ./master.yml ]; then
    echo "master.yml not found! Please create/rename as master.yml"
fi

if [ ! -f ./workers.yml ]; then
    echo "workers.yml not found! Please create/rename as workers.yml"
fi
#==============================================================================

# 2. Peg up master and workers; also fetch

## Master
peg up master.yml

## Workers
peg up workers.yml

## fetch
peg fetch $clustername
#==============================================================================

# 3. Install ssh aws and everything else

## ssh
peg install $clustername ssh
## aws
peg install $clustername aws
## hadoop
peg install $clustername hadoop
## spark
peg install $clustername spark
## Kafka
peg install $clustername kafka
## Kafka manager
peg install $clustername kafka-manager

## Start both the services
peg service $clustername hadoop start
peg service $clustername spark start
peg service $clustername kafka start
peg service $clustername kafka-manager start
