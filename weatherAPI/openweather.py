import requests
import math
import configparser
import json

config = configparser.ConfigParser();
config.read('config.ini')

# city_name = config['API']['city_name']
# api_key = config['API']['api_key']

city_name = "Webster,US"
api_key = "efe65d8cf2b9159616532ab27a555180"
zipcode = 95825

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    #print ("variables: ",)

    response = requests.get(url).json()
    #store json data
    with open('data.json', 'w') as f:
        json.dump(response,f)

    temp = response['main']['temp']
    temp = temp - 273.15 #convertion to celcius

    feels_like = response['main']['temp']
    feels_like = feels_like - 273.15 #convertion to celcius 

    humidity = response['main']['humidity']

    wind = response['wind']['speed']


    print(response)

    print("Local weather in " + city_name + " is:")
    print("Current Temperature: " , "%2.f" % temp , "°C")
    print("Feels Like: " , "%2.f" % feels_like , "°C")
    print("Humidity: " , humidity , "%")
    print("Wind: " , wind , " meters/sec")

def get_3day_forecast(api_key, city_name):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
    
    response = requests.get(url).json()
    #store json data
    with open('data3day.json', 'w') as f:
        json.dump(response,f)

get_weather(api_key, city_name)
get_3day_forecast(api_key,city_name)
