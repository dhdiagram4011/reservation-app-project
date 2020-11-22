from django.shortcuts import render
from django.http import HttpResponse
from .models import MsgPush
from .forms import *
from django.views.generic import ListView, View


## Class Type View
class MsgPushRepage(View): #web browser url path /push/sendev/
    def get(self,request):
        form = MsgPushForm(request.GET)
        return render(request, 'pushEngine/send.html', {'form':form})
    
    def post(self,request):
        form = MsgPushForm(request.POST)
        if form.is_valid():
            EKS_HOST = 'http://a8bdd5f7b96aa473ab24d95145037461-1710871681.ap-northeast-2.elb.amazonaws.com'
            STREAMING_HOST = 'http://a35f02dcb552449a3b4c0d0f708075b2-507238096.ap-northeast-2.elb.amazonaws.com:9000'
    
            STM_PATH = [
                "/auth/login",
                "/auth/register",
            ]
   
            for i in STM_PATH:
                URL_ALL = STREAMING_HOST + str(i.split(',')).replace('[','').replace(']','').replace('\'','')
                response = requests.get(URL_ALL)
                health_check = response.status_code ,':', URL_ALL.split(',')
                print(health_check)
                WEB_HOOK_URL = 'http://apis.aligo.in/send/'
                headers = {'Content-type':'application/x-www-form-urlencoded'}
                data = {
                    'key' : 'ubkm32s9fllu6ui96cq7uegwdk0oxhnc',
                    'user_id' : 'dhdiagram',
                    'sender' : request.POST['sender'],
                    'receiver' : request.POST['receiver'],
                    'destination' : request.POST['sender']|request.POST['sender'],
                    'msg' : health_check,
                    'title' : request.POST['title'],
                    'rdate' : '20201021',
                    'rtime'  : '1300',
                    'testmode_yn' : 'n'
                }
                requests.post(WEB_HOOK_URL, headers=headers, data=data)
        return HttpResponse("SUCCESS!!!")  


### Function Case View
def MsgSend(request):
    if request.method == 'GET':
        form = MsgPushForm(request.GET)
        return render(request, 'pushEngine/send.html', {'form':form})
    elif request.method == 'POST':
        form = sendForm(request.POST)
        if form.is_valid():
            EKS_HOST = 'http://a8bdd5f7b96aa473ab24d95145037461-1710871681.ap-northeast-2.elb.amazonaws.com'
            STREAMING_HOST = 'http://a35f02dcb552449a3b4c0d0f708075b2-507238096.ap-northeast-2.elb.amazonaws.com:9000'
    
        STM_PATH = [
            "/auth/login",
            "/auth/register",
        ]
   
        for i in STM_PATH:
            URL_ALL = STREAMING_HOST + str(i.split(',')).replace('[','').replace(']','').replace('\'','')
            response = requests.get(URL_ALL)
            health_check = response.status_code ,':', URL_ALL.split(',')
            print(health_check)
            WEB_HOOK_URL = 'http://apis.aligo.in/send/'
            headers = {'Content-type':'application/x-www-form-urlencoded'}
            data = {
                'key' : 'ubkm32s9fllu6ui96cq7uegwdk0oxhnc',
                'user_id' : 'dhdiagram',
                'sender' : request.POST['sender'],
                'receiver' : request.POST['receiver'],
                'destination' : request.POST['sender']|request.POST['sender'],
                'msg' : health_check,
                'title' : request.POST['title'],
                'rdate' : '20201011',
                'rtime'  : '1300',
                'testmode_yn' : 'n'
            }
            requests.post(WEB_HOOK_URL, headers=headers, data=data)
        return render(request, 'pushEngine/send_success.html')
