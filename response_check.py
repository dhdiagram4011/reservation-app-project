import requests
import json

def status_check():

    HOST = "http://13.125.124.194:8000"

    SVC_PATH = [
    '/admin', 
    '/auth/register', 
    '/auth/login',
    '/auth/logout', 
    '/auth/myinfo',
    '/auth/edit',
    '/auth/unregister',
    '/reservation/revstart',
    '/reservation/course_search',    
    '/reservation/date_search',
    '/reservation/date_search_result',
    '/reservation/ticketing_list',
    '/reservation/ticketing_list',
    '/revapi/seatmodify',
    '/revapi/schedulemodify',
    '/revapi/schedule_adding',
    '/revapi/register',
    '/revapi/seat',
    ] 
  
  
###print(SVC_PATH[0].split(','))  ### admin

    URL_0 = HOST + str(SVC_PATH[0].split(',')).replace('[','').replace(']','').replace('\'','') 
    URL_1 = HOST + str(SVC_PATH[1].split(',')).replace('[','').replace(']','').replace('\'','')
    URL_2 = HOST + str(SVC_PATH[2].split(',')).replace('[','').replace(']','').replace('\'','')
    URL_3 = HOST + str(SVC_PATH[3].split(',')).replace('[','').replace(']','').replace('\'','')
    URL_4 = HOST + str(SVC_PATH[4].split(',')).replace('[','').replace(']','').replace('\'','')
    URL_5 = HOST + str(SVC_PATH[5].split(',')).replace('[','').replace(']','').replace('\'','')
    URL_6 = HOST + str(SVC_PATH[6].split(',')).replace('[','').replace(']','').replace('\'','')
    URL_7 = HOST + str(SVC_PATH[7].split(',')).replace('[','').replace(']','').replace('\'','')
    URL_8 = HOST + str(SVC_PATH[8].split(',')).replace('[','').replace(']','').replace('\'','')
    URL_9 = HOST + str(SVC_PATH[9].split(',')).replace('[','').replace(']','').replace('\'','')
    URL_10 = HOST + str(SVC_PATH[10].split(',')).replace('[','').replace(']','').replace('\'','')


    #url = URL_1
    response = requests.get(URL_6)
    response.status_code
    print(response.status_code ,'+', SVC_PATH[6].split(','))




status_check()



