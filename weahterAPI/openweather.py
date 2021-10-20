import requests
import math
import configparser
config = configparser.ConfigParser();
config.read('config.ini')

city_name = config['API']['city_name']
api_key = config['API']['api_key']

#city_name = "Sacramento,US"
#api_key = "efe65d8cf2b9159616532ab27a555180"

def get_weather(api_key, city):
    config
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    print ("variables: ",)

    response = requests.get(url).json()
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


get_weather(api_key, city_name)
