### key : da740db95614eda666e49b3c867a0790

# # before sender auth
import requests
import time
import base64

url = 'https://sms.gabia.com/api/send/sms'
#payload = 'grant_type=client_credentials'
#data = 'TEST SMS API'
payload = 'phone=01021764011&callback=01021764011&message=SMS%20TEST%20MESSAGE&refkey=[[RESTAPITEST1549847130]]'
headers = {
'Content-Type':'application/x-www-form-urlencoded',
'Authorization':'Basic OTM0YjdhYzQyYTVmZDU1ODBjNDk1MDZkNzJkNzU5M2U'
}
response = requests.post(url, headers=headers, data=payload, allow_redirects=False)
print(response)
print(response.status_code)
print(response.text)
