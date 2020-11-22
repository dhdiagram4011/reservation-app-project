import requests

url = 'https://sms.gabia.com/api/send/sms'
payload = 'phone=01021764011&callback=01021764011&message=SMS%20TEST%20MESSAGE&refkey=[[RESTAPITEST1549847130]]' 
headers = {
    'Content-Type':'application/x-www-form-urlencoded',
    'Authorization':'Basic DckviEksLs6ZXlKMGVYQWlPaUpLVhiR2NpT2lKU1V6STFOaUo5LmV5SnBjM01pT2lKb2RIUndjenBjTDF3dmMyMXpMbWRoWW1saExtTnZiVnd2SWl3aVlYVmtJam9pWEM5dllYVjBhRnd2ZEc5clpXNGlMQ0pshWFhnT2pBNG5uVkVuLWtnVEJoRGpPeWc='
}
response = requests.request('POST',url, headers=headers, data=payload, allow_redirects=False, timeout=1)


