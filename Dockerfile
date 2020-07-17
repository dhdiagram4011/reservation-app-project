FROM centos:7
WORKDIR /app
RUN yum install wget -y ; yum install git -y ; yum install python3-* -y ; yum install python3-pip -y
###RUN wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
###RUN sh /app/Anaconda3-2020.02-Linux-x86_64.sh -y
###RUN conda create --name ticket-app-develop python=3.7 -y
RUN git clone -b develop https://github.com/dhdiagram4011/reservation-app-project.git
### CMD cd /app/reservation-app-project
RUN pip3 install Django==2.1.5 ; pip3 install autopep8 ; pip3 install pylint
RUN yum update -y
EXPOSE 80
CMD nohup python3 /app/reservation-app-project/manage.py runserver 0:80 &
