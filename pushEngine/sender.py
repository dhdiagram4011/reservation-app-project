# curl -X POST "http://apis.aligo.in/send/" \
# 	--data-urlencode "key=eqsuxrlee16gdfcj3u5j8j4qvq70brkn" \
# 	--data-urlencode "user_id=dhdiagram" \
# 	--data-urlencode "sender=01000000000" \
# 	--data-urlencode "receiver=0100000000,0100000000" \
# 	--data-urlencode "destination=0100000000|홍길동" \
# 	--data-urlencode "msg=%홍길동%님! 안녕하세요. API TEST SEND 입니다" \
# 	--data-urlencode "title=API TEST 입니다" \
# 	--data-urlencode "rdate=20201010" \
# 	--data-urlencode "rtime=1302" \
# 	--data-urlencode "testmode_yn=Y"

from urllib.request import urlopen
import requests
import json

def status_check():

    EKS_HOST = 'http://a8bdd5f7b96aa473ab24d95145037461-1710871681.ap-northeast-2.elb.amazonaws.com'
    STREAMING_HOST = 'http://a35f02dcb552449a3b4c0d0f708075b2-507238096.ap-northeast-2.elb.amazonaws.com:9000'

    SVC_PATH = [
    "/admin", 
    "/auth/register", 
    "/auth/login",
    "/auth/logout", 
    "/auth/myinfo",
    "/auth/edit",
    "/auth/unregister",
    "/reservation/revstart",
    "/reservation/course_search",    
    "/reservation/date_search",
    "/reservation/date_search_result",
    "/reservation/ticketing_list",
    "/revapi/seatmodify",
    "/revapi/schedulemodify",
    "/revapi/schedule_adding",
    "/revapi/register",
    "/revapi/seat",
    ]

    STM_PATH = [
        "/auth/login",
        "/auth/register",
    ]


    for i in SVC_PATH:

        URL_ALL = EKS_HOST + str(i.split(',')).replace('[','').replace(']','').replace('\'','')
        response = requests.get(URL_ALL)
        health_check = response.status_code ,':', URL_ALL.split(',')
        print(health_check)

        WEB_HOOK_URL = 'http://apis.aligo.in/send/'
        headers = {'Content-type':'application/x-www-form-urlencoded'}
        #data = {'text':json.dumps(health_check)}
        data = {
        'key' : 'ubkm32s9fllu6ui96cq7uegwdk0oxhnc',
        'user_id' : 'dhdiagram',
        'sender' : '01021764011',
        'receiver' : '01021764011',
        'destination' : '01021764011|김도형',
        'msg' : health_check,
        'title' : 'API TEST 입니다',
        'rdate' : '20201011',
        'rtime'  : '1245',
        'testmode_yn' : 'n'
       }
        requests.post(WEB_HOOK_URL, headers=headers, data=data)
        #requests.post(WEB_HOOK_URL, headers=headers, data='{"text":"FFF!"}') ### slack sample 


    for i in STM_PATH:

        URL_ALL = STREAMING_HOST + str(i.split(',')).replace('[','').replace(']','').replace('\'','')
        response = requests.get(URL_ALL)
        health_check = response.status_code ,':', URL_ALL.split(',')
        print(health_check)
        WEB_HOOK_URL = 'http://apis.aligo.in/send/'
        headers = {'Content-type':'application/x-www-form-urlencoded'}
        #data = {'text':json.dumps(health_check)}
        data = {
        'key' : 'ubkm32s9fllu6ui96cq7uegwdk0oxhnc',
        'user_id' : 'dhdiagram',
        'sender' : '01021764011',
        'receiver' : '01021764011',
        'destination' : '01021764011|김도형',
        'msg' : health_check,
        'title' : 'API TEST 입니다',
        'rdate' : '20201011',
        'rtime'  : '1300',
        'testmode_yn' : 'n'
        }
        requests.post(WEB_HOOK_URL, headers=headers, data=data)
        #requests.post(WEB_HOOK_URL, headers=headers, data='{"text":"FFF!"}') ### slack sample 


status_check()





