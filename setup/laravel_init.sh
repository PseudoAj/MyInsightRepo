#!/bin/bash

#title           :laravel_init.sh
#description     :The script will create a new laravel project
#author		       :Ajay Krishna Teja Kavuri
#date            :02062017
#version         :0.1
#==============================================================================

# variables
PROJECT_NAME="auth"
WEB_ROOT="/var/www/html/"
PROJECT_DIR="/home/ubuntu/MyInsightRepo/laravel/"
CONF_PATH="/etc/apache2/apache2.conf"
PRJCT_CONF="/home/ubuntu/MyInsightRepo/misc/apache2.conf"

# Remove if something already exists
sudo rm -rf $WEB_ROOT$PROJECT_NAME

# Change the directory
cd $PROJECT_DIR

# Create a sample laravel project
# laravel new project-css
composer create-project --prefer-dist laravel/laravel $PROJECT_NAME

# Move into Apache
sudo mv $PROJECT_DIR$PROJECT_NAME $WEB_ROOT

# Set the configurations
chmod 775 $WEB_ROOT$PROJECT_NAME
sudo chown -R www-data:www-data $WEB_ROOT$PROJECT_NAME
sudo chmod 755 /var/www
sudo rm -R $CONF_PATH
sudo ln -s $PRJCT_CONF /etc/apache2
sudo service apache2 restart
