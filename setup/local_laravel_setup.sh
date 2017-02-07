#!/bin/bash

#title           :local_laravel_setup.sh
#description     :The script will setup an existing laravel project in local mode
#author		       :Ajay Krishna Teja Kavuri
#date            :02062017
#version         :0.1
#==============================================================================

# variables
PROJECT_NAME="auth"
WEB_ROOT="/var/www/html/"
PROJECT_DIR="/home/pseudoaj/GitHubRepos/MyInsightRepo/laravel/"
CONF_PATH="/etc/apache2/apache2.conf"
PRJCT_CONF="/home/pseudoaj/GitHubRepos/MyInsightRepo/misc/apache2.conf"

# Remove if something already exists
sudo rm -rf $WEB_ROOT$PROJECT_NAME

# Move into Apache
sudo cp -R $PROJECT_DIR$PROJECT_NAME $WEB_ROOT

# Set the configurations
sudo chmod 775 $WEB_ROOT$PROJECT_NAME
sudo chown -R www-data:www-data $WEB_ROOT$PROJECT_NAME
sudo chmod 755 /var/www
sudo rm -R $CONF_PATH
sudo ln -s $PRJCT_CONF /etc/apache2
sudo service apache2 restart
