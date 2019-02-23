#Weather API
import requests
import json

url = 'http://ip-api.com/json'

r = requests.get(url)
if r.status_code >= 200 < 400:
    data = r.text
    print(data)
    result = json.loads(data)
    print(result)
