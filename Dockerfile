FROM digglerz/python3.8

MAINTAINER dhdiagram@gmail.com
EXPOSE 8000
WORKDIR /app
ADD . /app
RUN pip3 install djangorestframework
RUN pip3 install Django==2.1.5
RUN python3 manage.py migrate
RUN python3 manage.py makemigrations
CMD ["python3" ,"manage.py", "runserver", "0.0.0.0:8000"]