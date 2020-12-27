#!/bin/bash

cd /home/ec2-user/app
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0:8000 &
