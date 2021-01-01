#!/bin/bash

sudo python3 /home/ec2-user/apps/manage.py makemigrations
sudo python3 /home/ec2-user/apps/manage.py migrate
source /home/ec2-user/apps/twilio.env
##sudo python3 /home/ec2-user/apps/manage.py runserver 0:8000 & \


