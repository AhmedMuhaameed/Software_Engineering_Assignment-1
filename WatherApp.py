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
#==============================================================
    url = 'http://api.aladhan.com/v1/currentTimestamp?zone=' + timeZone
    request = requests.get(url)
    if request.status_code >= 200 < 400:
        data = json.loads(request.text)
        timeStamp = data['data']

        url = 'http://api.aladhan.com/v1/timings/+' + timeStamp \
              + '?latitude=' + str(lat) + '&longitude=' + str(lon) + '&method=2'
        request = requests.get(url)
        if request.status_code >= 200 < 400:
            data = json.loads(request.text)

            dateNum = data['data']['date']['hijri']['date']

            dataStr = str(data['data']['date']['hijri']['day']) \
                      + ' ' + str(data['data']['date']['hijri']['month']['ar']) \
                      + ' ' + str(data['data']['date']['hijri']['year'])
            print(dateNum)
            print(dataStr + '\n')

            fajrTime = data['data']['timings']['Fajr']
            print('Fajr: ' + fajrTime)

            sunriseTime = data['data']['timings']['Sunrise']
            print('Sunrise: ' + sunriseTime)

            dhuhrTime = data['data']['timings']['Dhuhr']
            print('Dhuhr: ' + dhuhrTime)

            asrTime = data['data']['timings']['Asr']
            print('Asr: ' + asrTime)

            sunsetTime = data['data']['timings']['Sunset']
            print('Sunset: ' + sunsetTime)

            maghribTime = data['data']['timings']['Maghrib']
            print('Maghrib: ' + maghribTime)

            ishaTime = data['data']['timings']['Isha']
            print('Isha: ' + ishaTime)

            url = 'http://api.aladhan.com/v1/currentTime?zone=' + timeZone
            request = requests.get(url)
            if request.status_code >= 200 < 400:
                data = json.loads(request.text)

                time = data['data']
                print('\n\nTime Now: ' + time)
