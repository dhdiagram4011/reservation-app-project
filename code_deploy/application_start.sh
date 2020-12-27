#!/bin/bash

cd /home/ec2-user/app
sudo yum install python3* -y
sudo pip3 install Django==2.1.5
sudo pip3 install pylint
sudo pip3 install djangorestframework
sudo pip3 install request
python3 /home/ec2-user/app/manage.py makemigrations
python3 /home/ec2-user/app/manage.py migrate
nohup python3 /home/ec2-user/app/manage.py runserver 0:8000 &
