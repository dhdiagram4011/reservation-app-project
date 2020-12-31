#!/bin/bash

sudo yum update -y
sudo rm -rf /home/ec2-user/*
sudo mkdir -p /home/ec2-user/apps
cd /home/ec2-user/apps
sudo git clone -b develop https://github.com/dhdiagram4011/reservation-app-project.git .
sudo yum remove python3* -y
sudo yum install python3* -y
sudo pip3 install djangorestframework
sudo pip3 install Django==2.1.5
sudo pip3 install pylint
sudo pip3 install requests
sudo pip3 install twilio
