import requests
import json

noti_url = 'https://hooks.slack.com/services/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'
headers = {'Content-Type':'application/json'}


def main_host(requests):

    main_host = 'http://35.225.159.194:8100'
    response = requests.get(main_host)
    result = response.status_code

    if str(result) in "200":
        data = {"text":"main host page status_code check success"} 
        requests.post(noti_url, headers=headers, data=json.dumps(data))
    else:
        data = {"text":"main host page check!!!"} 
        requests.post(noti_url, headers=headers, data=json.dumps(data))


def registration_page(requests):

    registration_page = 'http://35.225.159.194:8100/auth/register'
    response = requests.get(registration_page)
    result = response.status_code

    if str(result) in "200":
        data = {"text":"registration_page status_code check success"} 
        requests.post(noti_url, headers=headers, data=json.dumps(data))
    else:
        data = {"text":"registration_page check!!!"} 
        requests.post(noti_url, headers=headers, data=json.dumps(data))


def admin_page(requests):

    admin_page = 'http://35.225.159.194:8100/admin'
    response = requests.get(admin_page)
    result = response.status_code

    if str(result) in "200":
        data = {"text":"admin_page status_code check success"} 
        requests.post(noti_url, headers=headers, data=json.dumps(data))
    else:
        data = {"text":"admin_page check!!!"} 
        requests.post(noti_url, headers=headers, data=json.dumps(data))


def login_page(requests):

    login_page = 'http://35.225.159.194:8100/auth/login'
    response = requests.get(login_page)
    result = response.status_code

    if str(result) in "200":
        data = {"text":"login page status_code check success"} 
        requests.post(noti_url, headers=headers, data=json.dumps(data))
    else:
        data = {"text":"login page check!!!"} 
        requests.post(noti_url, headers=headers, data=json.dumps(data))


def reservation_page(requests):

    reservation_page = 'http://35.225.159.194:8100/reservation/revstart'
    response = requests.get(reservation_page)
    result = response.status_code

    if str(result) in "200":
        data = {"text":"reservation_page status_code check success"} 
        requests.post(noti_url, headers=headers, data=json.dumps(data))
    else:
        data = {"text":"reservation_page check!!!"} 
        requests.post(noti_url, headers=headers, data=json.dumps(data))


def date_page(requests):

    date_page = 'http://35.225.159.194:8100/reservation/date_search/'
    response = requests.get(date_page)
    result = response.status_code

    if str(result) in "200":
        data = {"text":"date page status_code check success"} 
        requests.post(noti_url, headers=headers, data=json.dumps(data))
    else:
        data = {"text":"date page check!!!"} 
        requests.post(noti_url, headers=headers, data=json.dumps(data))


main_host(requests)
registration_page(requests)
admin_page(requests)
login_page(requests)
reservation_page(requests)
date_page(requests)