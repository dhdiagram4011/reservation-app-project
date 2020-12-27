#!/bin/bash

cd /home/ec2-user/app
python3 /home/ec2-user/app/manage.py makemigrations
python3 /home/ec2-user/app/manage.py migrate
python3 /home/ec2-user/app/manage.py runserver 0:8000 &
