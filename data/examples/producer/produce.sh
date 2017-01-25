#!/bin/bash

#title           :produce.sh
#description     :The script will simulate multiple producers
#author		       :Ajay Krishna Teja Kavuri
#date            :01252017
#version         :0.1
#==============================================================================

# Get the arguments
IP_ADDR=$1
NUM_SPAWNS=$2
SESSION=$3

# Create a new session in tmux
tmux new-session -s $SESSION -n bash -d

# trigger the script
for ID in `seq 1 $NUM_SPAWNS`;
do
    echo $ID
    tmux new-window -t $ID
    tmux send-keys -t $SESSION:$ID 'python producer.py '"$IP_ADDR"' '"$ID"'' C-m
done
