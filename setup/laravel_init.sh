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
PROJECT_DIR="MyInsightRepo/laravel/"

# Remove if something already exists
sudo rm -rf $WEB_ROOT$PROJECT_NAME

# Change the directory
cd ~
cd $PROJECT_DIR

# Create a sample laravel project
# laravel new project-css
composer create-project --prefer-dist laravel/laravel $PROJECT_NAME

# Move into Apache
sudo mv $PROJECT_DIR$PROJECT_NAME $WEB_ROOT

# Set the configurations
chmod 775 $WEB_ROOT$PROJECT_NAME
sudo chown -R apache:apache $WEB_ROOT$PROJECT_NAME
sudo chmod 755 /var/www
# sudo rm -R /etc/httpd/conf/httpd.conf
# sudo ln -s /vagrant/serverConfiguration/httpd.conf /etc/httpd/conf
sudo service apache2 restart
