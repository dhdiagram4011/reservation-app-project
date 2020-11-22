### key : da740db95614eda666e49b3c867a0790

# # before sender auth
import requests
import time

url = 'https://sms.gabia.com/oauth/token'
payload = 'grant_type=client_credentials'
data = "TESTAPI is Send"
headers = {
'Content-Type':'application/x-www-form-urlencoded',
'Authorization':'Basic fdc1cb65bdcb6b2629bb8104593697dc'
}
###response = requests.request('POST', url, headers=headers, data=payload, allow_redirects=False)

response = requests.request('POST', url, headers=headers, data=data)
print(response)
print(response.status_code)
print(response.text)
