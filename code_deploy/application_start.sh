#!/bin/bash

sudo rm -rf /home/ec2-user/app/*
sudo rm -rf /home/ec2-user/app/.*
sudo yum update -y
mkdir -p /home/ec2-user/app
chown -R ec2-user:ec2-user /home/ec2-user/app
cd /home/ec2-user/app
sudo yum remove python3* -y
sudo yum install python3* -y
pip3 install djangorestframework
pip3 install Django==2.1.5
pip3 install pylint
pip3 install requests
pip3 install twilio
python3 /home/ec2-user/app/manage.py makemigrations
python3 /home/ec2-user/app/manage.py migrate
