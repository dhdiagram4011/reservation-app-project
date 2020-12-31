#!/bin/bash

sudo -i
yum update -y
mkdir -p /root/apps
yum remove python3* -y
yum install python3* -y
pip3 install djangorestframework
pip3 install Django==2.1.5
pip3 install pylint
pip3 install requests
pip3 install twilio


