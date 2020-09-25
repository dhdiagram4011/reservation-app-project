FROM yosugi/cron-centos

MAINTAINER dhdiagram@gmail.com
EXPOSE 8001
WORKDIR /app
ADD ./response_check.py /app
ADD ./blank.py /app
RUN yum install python3 python3-pip crond crontab -y
RUN pip3 install requests
CMD /etc/crontab >> 05 * * * * python3 /app/response_check.py
CMD systemctl enable crond
CMD systemctl start crond
CMD ["nohup", "python3" ,"/app/blank.py"]