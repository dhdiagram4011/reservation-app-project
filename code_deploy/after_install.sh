#!/bin/bash

sudo yum update -y
mkdir -p /home/ec2-user/apps
yum remove python3* -y
yum install python3* -y
sudo pip3 install djangorestframework
sudo pip3 install Django==2.1.5
sudo pip3 install pylint
sudo pip3 install requests
sudo pip3 install twilio


