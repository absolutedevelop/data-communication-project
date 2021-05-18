#!/bin/bash

#Create the website folders
sudo mkdir -p /var/www/music
#sudo mkdir -p /var/www/music/public_html
#sudo mkdir -p /var/www/kitpro

#set permissions on the folder
sudo chmod -R 755 /var/www

#create html code TODO: copy the file to the folder
sudo touch /var/www/music/index.html
#sudo touch /var/www/music/index/html

#set the permissions fo the index file
sudo chmod -R 755 /var/www/

#create a virtual host config files
sudo touch /etc/apache2/sites-available/music.web.conf
#make file writable
sudo chmod -R a+rwX /etc/apache2/sites-available/music.web.conf

#write config file
sudo cat confi > /etc/apache2/sites-available/music.web.conf

#enable config file
cd /etc/apache2/sites-available/
sudo a2ensite music.web.conf

#restart apache
#sudo systemctl apache2
#sudo a2dissite 000-default.conf







