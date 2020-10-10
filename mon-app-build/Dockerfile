FROM alpine
MAINTAINER dhdiagram@gmail.com
EXPOSE 8001
WORKDIR /app
ADD ./response_check.py /app
ADD ./blank.py /app
RUN apk add --update python3 py3-pip
RUN apk add tzdata
RUN cp /usr/share/zoneinfo/Asia/Seoul /etc/localtime
RUN pip3 install requests
RUN echo '35 * * * * python3 /app/response_check.py' > /etc/crontabs/root
CMD ["crond"]
CMD ["nohup","python3","/app/blank.py"]
