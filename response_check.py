import requests
import json

## slack url : https://app.slack.com/client/T01A7E44RNX/C01A7E451KM
## app id : A01A45QN893
## client id : 1347480161779.1344194756309
## client secret : 95f9885ab57cb0890204cff436132866
## veri token : wRznTSY59HfrQmPJSc6lb5Mb
## webhook url : https://hooks.slack.com/services/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


def status_check():

    FARGATE_HOST = 'http://13.125.124.194:8000'

    SVC_PATH = (
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
    )



    for i in SVC_PATH:

        URL_ALL = FARGATE_HOST + str(i.split(',')).replace('[','').replace(']','').replace('\'','')
        #URL_ALL = FARGATE_HOST + str(i)
        response = requests.get(URL_ALL)
        health_check = response.status_code ,':', URL_ALL.split(',')
        print(health_check)
        
        WEB_HOOK_URL = 'https://hooks.slack.com/services/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'
        headers = {'Content-type':'application/json'}
        requests.post(WEB_HOOK_URL, headers=headers, data=json.dumps(health_check))
        #requests.post(WEB_HOOK_URL, headers=headers, data='{"text":"FFF!"}')

status_check()
