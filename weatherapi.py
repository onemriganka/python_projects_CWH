import requests
import json

city = input("enter the name of your city = \n")

url = f" http://api.weatherapi.com/v1/current.json?key=38428d5142934ab5b78152514231110&q={city}&aqi=no"

r = requests.get(url)
# print(r.text)

wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])
