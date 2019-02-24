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
#Weather API
api_key = '9bb4b43bf13147ef8628e69c31b866ad';
url = 'https://api.weatherbit.io/v2.0/current?city=' + user_location + '&key=' + api_key

request = requests.get(url)
if request.status_code >= 200 < 400:
    data = json.loads(request.text)
    city = user_location
    temp = data['data'][0]['temp']
    desc = data['data'][0]['weather']['description']

    main_msg = 'City: ' + city + '\n' +\
               'Temp: ' + str(temp) + '\n' +\
               'Description: ' + desc + '\n'
    print(main_msg)

    lat = data['data'][0]['lat']
    lon = data['data'][0]['lon']
    timeZone = data['data'][0]['timezone']
#=========================================== End of Weather api
