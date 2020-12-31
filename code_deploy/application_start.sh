#!/bin/bash


python3 /home/ec2-user/apps/manage.py makemigrations
python3 /home/ec2-user/apps/manage.py migrate

