FROM digglerz/python3.8

MAINTAINER dhdiagram@gmail.com
EXPOSE 80
WORKDIR /app
ADD . /app
RUN pip3 install twilio
RUN pip3 install djangorestframework
RUN pip3 install Django==2.1.5
RUN pip3 install requests
RUN python3 manage.py migrate
RUN python3 manage.py makemigrations
CMD ["python3" ,"manage.py", "runserver", "0.0.0.0:80"]
