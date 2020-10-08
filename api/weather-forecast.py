"""
      It's also a web-scraping script but the difference is, for getting data from a website we need a api key.
      I am scraping https://openweathermap.org for getting weather data with the help of their api service.
      As i am using a free api key which has a limit of 60 calls/minute, if more user use this api key the limit
            can be over. Then you have two options
            1 -> wait for ending the time limit
            2 -> get your own api key. Don't worry. It's very easy and free. You don't need to know about api
                Just follow these steps
                i) go to https://openweathermap.org/price
                ii) choose 'Daily Forecast 16 days' and click subscribe and choose free plan
                iii) create free account with your email and verify that
                iv) copy your api key from your account and replace it with my API_KEY in this script. Ex.
                        API_KEY = 'your api key'
                v) run the script
      Note: Try to use your own api key. It will give you better performance
"""

import requests
import json
from termcolor import colored
import os

# showing usage of the script
print(colored("\nhttps://openweathermap.org will be used to get weather data. Type 'exit' to stop the code and "
              "'clear' to clean the console\nIn this script a free api "
              "service is used which has a limit of 60 calls per minute. So if more user use this script then search "
              "limit will over. Then you have two options one is waiting and another is get your personal API key. "
              "Its pretty easy. go to https://openweathermap.org/price. select 'Daily Forecast 16 days' and subscribe "
              "for free key. After that simply replace the API key in this script. That's it... Happy scripting !!!",
              'yellow'))

API_KEY = 'b0e89de16c36159c886bf9900abee841'

while True:
    location = "+".join(input("\nLocation : ").lower().split(" "))
    if location == 'exit':
        break
    if location == 'clear':
        os.system('clear')
        continue
    try:
        page = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=' + location +'&appid=' + API_KEY)
        data = json.loads(page.content)

        temp_date = 0
        for i in data['list']:
            date = i['dt_txt'].split(' ')[0]
            time = i['dt_txt'].split(' ')[1]
            temp = round(float(i['main']['temp']) - 273, 2)
            min_temp = round(float(i['main']['temp_min']) - 273, 2)
            max_temp = round(float(i['main']['temp_max']) - 273, 2)
            feel_temp = round(float(i['main']['feels_like']) - 273, 2)
            pressure = round(float(i['main']['sea_level']))
            sea_level = round(float(i['main']['sea_level']))
            grnd_level = round(float(i['main']['grnd_level']))
            humidity = round(float(i['main']['humidity']))
            wind_speed = i['wind']['speed']
            wind_angle = i['wind']['deg']
            main = i['weather'][0]['main']
            description = i['weather'][0]['description']
            if temp_date != date:
                print(colored("Date :" + str(date), 'green'), end="")
                temp_date = date
            print("""
            Time : {}
                Temperature : {:<5}          |  Pressure   : {:<6}  |  Wind speed : {}
                Minimum temperature : {:<5}  |  Sea level  : {:<6}  |  Wind angle : {}
                Maximum temperature : {:<5}  |  Grnd level : {:<6}  |  Main : {}
                Feels like : {:<5}           |  Humidity   : {:<6}  |  Description : {}
                """.format(time, temp, pressure, wind_speed, min_temp, sea_level, wind_angle, max_temp, grnd_level, main, feel_temp, humidity, description))
    except:
        print("Something went wrong. Couldn't find data")
    print()
