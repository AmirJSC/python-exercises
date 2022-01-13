#! python3
#  getOpenWeather.py - Prints the weather for a location from the command line

APPID = '9e7063924bad54b358431fb70bf80478'
#Requests are formatted as city, comma, then the country code like PH, US etc.

import json, requests, sys, os

os.chdir('C:\\Pythoncode')

if len(sys.argv) < 2:
    print('Usage: quickweather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from openweathermap.org's API
url ='http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (location, APPID)
response = requests.get(url)


# Load JSON data into Python variable.
w = json.loads(response.text)

# Uncomment to see the raw JSON text:
print(response.text)


print('Current weather in %s:' % (location))
print(w['weather'][0]['main'], '-', w['weather'][0]['description'])

