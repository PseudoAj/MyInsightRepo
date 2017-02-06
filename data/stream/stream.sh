#!/bin/bash

#title           :stream.sh
#description     :The script is to trigger the straming events
#author		       :Ajay Krishna Teja Kavuri
#date            :02022017
#version         :0.1
#==============================================================================
# Reading arguments

## duration for the stream
read -p "Please enter duration for stream in days (Ex: 1 ): " strmDur
strmDur=${strmDur}

## interval for the stream
read -p "Please enter interval for stream in seconds (Ex: 5 ): " intrvl
intrvl=${intrvl}

SESSION='de-ny-ajay-stream'
#==============================================================================

# New tmux session
tmux new-session -s $SESSION -n bash -d

# Create a new window for electricity data
ElecID=1
tmux new-window -t $ElecID
tmux send-keys -t $SESSION:$ElecID 'python electricity.py '"$strmDur"' '"$intrvl"'' C-m
echo "Electricity stream started."

# Create a new window for water data
# WtrID=2
# tmux new-window -t $WtrID
# tmux send-keys -t $SESSION:$WtrID 'python electricity.py '"$strmDur"' '"$intrvl"'' C-m
# echo "Water stream started."
