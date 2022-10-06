import requests
import os
from datetime import datetime

user_api="f7ca2b696cb13d2657bd578258701fb3"
location=input("Enter the City Name")
complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link=requests.get(complete_api_link)
api_data=api_link.json()
if api_data['cod']=='404':
    print('Invalid City: {} ,Please Check Your City Name'.format(location))
else:
    temp_city=((api_data['main']['temp'])-273.15)
    weather_desc=api_data['weather'][0]['description']
    hmdt=api_data['main']['humidity']
    wind_spd=api_data['wind']['speed']
    date_time=datetime.now().strftime("%d %b %Y | %I:%M:%S %p ")
    
    
    print("--------------------------------------------------")
    print("weather stats for {} || {}".format(location.upper(),date_time))
    print("--------------------------------------------------")
    print("Cuurent Temperature is {:.2f} deg C".format(temp_city))
    print("current Weather Desc :",weather_desc)
    print("Current  Humidity    :",hmdt,"%")
    print("Current wind Speed   :",wind_spd,'kmph')
    