#!/usr/bin/env bash  

yum update -y  
yum install -y python3 
yum install -y python3-pip 
pip3 install autopep8 
pip3 install pylint 
pip3 install Django==2.1.5 
pip3 install djangorestframework
python3 /vagrant/manage.py migrate 
python3 /vagrant/manage.py makemigrations 
nohup python3 /vagrant/manage.py runserver 0:8888 & 

