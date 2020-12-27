#!/bin/bash

sudo -i
yum update -y
cd /home/ec2-user/app
yum install python3* -y
pip3 install Django==2.1.5
pip3 install pylint
pip3 install djangorestframework
pip3 install requests
pip3 install twilio
python3 /home/ec2-user/app/manage.py makemigrations
python3 /home/ec2-user/app/manage.py migrate
