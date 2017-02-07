#!/bin/bash

#title           :lamp_setup.sh
#description     :The script will install all the required packages for laravel
#author		       :Ajay Krishna Teja Kavuri
#date            :02062017
#version         :0.1
#==============================================================================

# Formal update for no reason
sudo apt-get -y update

# Setup for packages
sudo add-apt-repository -y ppa:ondrej/php

# Install apache
sudo apt-get -y install apache2
echo -e "----Installed Apache----\n\n"

# Install MySQL
sudo apt-get -y install mysql-server
echo -e "----Installed MySQL----\n\n"

# Install PHP 7
sudo apt-get install -y libapache2-mod-php7.0 php7.0-fpm php7.0-common php7.0-cli php-pear php7.0-curl php7.0-gd php7.0-gmp php7.0-intl php7.0-imap php7.0-json php7.0-ldap php7.0-mbstring php7.0-mcrypt php7.0-mysql php7.0-ps php7.0-readline php7.0-tidy php7.0-xmlrpc php7.0-xsl
echo -e "----Installed PHP 7----\n\n"

# Start and set apache
sudo service apache2 start
sudo service apache2 enable
echo -e "----Started Apache----\n\n"

# Start and set MySQl
sudo service mysql start
sudo service mysql enable
echo -e "----Started MySQL----\n\n"

# Install Node, gulp and libnotify
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install -y nodejs
echo -e "----Installed Node and npm----\n\n"

# Install composer
curl -sS https://getcomposer.org/installer | php
sudo chmod +x composer.phar
sudo mv composer.phar /usr/bin/composer
echo -e "----Installed composer----\n\n"
