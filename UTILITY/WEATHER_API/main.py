from bs4.builder import HTML
import requests
import json
from bs4 import BeautifulSoup
api_key = '6fac953faaa5adb6e5a26491db066eee'
city = 'vidisha'
country = 'india'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country},lang = hi&appid={api_key}'

req  = requests.get(url)
print(req.status_code)
data = req.json()
# print(type(data))
json_obj = json.dumps(data,indent=4)
# print(type(json_obj))
print(json_obj) 
# print(type(json_obj))
rain  =None
for key in data:
    if key == 'rain':
        rain = data[key]
        continue
    if key == 'weather':
        weather = data[key]
        continue
    if key == 'clouds':
        clouds = data[key]
        continue
    if key == 'main':
        main  = data[key]
        continue


# to convert form kelvin to celsius 
#  273.15 
tmp = main['temp']
humd = main['humidity']
clouds  = main['clouds']