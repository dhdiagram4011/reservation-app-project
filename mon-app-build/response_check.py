import requests
import json

## slack url : https://app.slack.com/client/T01A7E44RNX/C01A7E451KM
## app id : A01A45QN893
## client id : 1347480161779.1344194756309
## client secret : 95f9885ab57cb0890204cff436132866
## veri token : wRznTSY59HfrQmPJSc6lb5Mb
## webhook url : https://hooks.slack.com/services/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


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

        WEB_HOOK_URL = 'https://hooks.slack.com/services/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'
        headers = {'Content-type':'application/json'}
        data = {'text':json.dumps(health_check)}
        requests.post(WEB_HOOK_URL, data=json.dumps(data), headers=headers)
        #requests.post(WEB_HOOK_URL, headers=headers, data='{"text":"FFF!"}') ### slack sample 


    for i in STM_PATH:

        URL_ALL = STREAMING_HOST + str(i.split(',')).replace('[','').replace(']','').replace('\'','')
        response = requests.get(URL_ALL)
        health_check = response.status_code ,':', URL_ALL.split(',')
        print(health_check)

        WEB_HOOK_URL = 'https://hooks.slack.com/services/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'
        headers = {'Content-type':'application/json'}
        data = {'text':json.dumps(health_check)}
        requests.post(WEB_HOOK_URL, data=json.dumps(data), headers=headers)
        #requests.post(WEB_HOOK_URL, headers=headers, data='{"text":"FFF!"}') ### slack sample 


status_check()
