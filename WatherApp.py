 # Weather API
import requests # pip install requests
import json # pip install simplejson

user_location = 'London,UK'

# IP API
url = 'http://ip-api.com/json'
requestLocation = requests.get(url)
if requestLocation.status_code >= 200 < 400:
	data = json.loads(requestLocation.text)
	user_location = data['city'] + ',' + data['countryCode']

#==============================================================
# Weather API
api_key = '9bb4b43bf13147ef8628e69c31b866ad'
location = 'Cairo,EG'
url = 'https://api.weatherbit.io/v2.0/current?city=' + location + '&key=' + api_key
r = requests.get(url)
status = r.status_code
if status >= 200 < 400:
	data = r.text
	result = json.loads(data)
	print(data)
	print(result)
#=========================================== End of Weather api
