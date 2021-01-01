#!/bin/bash

sudo python3 /home/ec2-user/apps/manage.py makemigrations
sudo python3 /home/ec2-user/apps/manage.py migrate
source /home/ec2-user/apps/pushEngine/twilio.env
python3 /home/ec2-user/apps/pushEngine/twillio.py


