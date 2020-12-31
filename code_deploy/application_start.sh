#!/bin/bash

sudo -i
python3 /root/apps/manage.py makemigrations
python3 /root/apps/manage.py migrate
