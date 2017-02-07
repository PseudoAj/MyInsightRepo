#!/bin/bash

#title           :sync_local_laravel.sh
#description     :The script will sync for any updates
#author		       :Ajay Krishna Teja Kavuri
#date            :02062017
#version         :0.1
#==============================================================================

# Sunc the folders
sudo rsync -tr /home/pseudoaj/GitHubRepos/MyInsightRepo/laravel/auth/* /var/www/html/auth/

# run the mix to update style
cd /var/www/html/auth/
sudo npm run dev

# Comeback
cd /home/pseudoaj/GitHubRepos/MyInsightRepo/setup
