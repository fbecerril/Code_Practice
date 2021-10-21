"""
Author: Francisco Becerril
Description: Weatherbit.io API call
"""
from csv_write import *
import requests
import json


#API Parameters
key = "27b60a99e42045949ef29f2798b73728"
units = "I"     #I = imperial M = metric
zipcode = "95825"
city = "Sacramento"
cityAndState = "Sacramento,CA"
State = "CA"
Country = "US"

#output lists
current_values =[]
threeDay_values = []

def current():
    url = f"https://api.weatherbit.io/v2.0/current?&city={cityAndState}&key={key}"
    response = requests.get(url).json()
    #write results into json file
    with open("weatherbit.json",'w') as file_object:
        json.dump(response,file_object,indent=4)
    #append data to csv
    #observed time
    obs = response['data'][0]['ob_time']
    current_values.append(obs[0:10])
    current_values.append(obs[11:16])
    #wind speed
    current_values.append(response["data"][0]["wind_spd"])
    #wind direction
    current_values.append(response["data"][0]["wind_cdir"])
    #chance of rain (not available in current)
    #current_values.append(response["data"][0]["pop"]) 
    #precipitation volume
    current_values.append(response["data"][0]["precip"])
    
    #print list
    print(current_values)
    csv_input(current_values)

def threeDay():
    url = f"https://api.weatherbit.io/v2.0/forecast/daily?&city={cityAndState}&key={key}&units={units}&days=3"
    response = requests.get(url).json()
    #write results into json file
    with open("weatherbit3day.json",'w') as file_object:
        json.dump(response,file_object,indent=4) 
    #append data to csv

    print(response["data"][1]["wind_spd"])

def timechange(hour):
    #make adjustment
    if(hour < 7):
        new_hour = 24 - (7 - hour)
    else:
        new_hour = hour - 7
    #proper format
    if(new_hour < 10):
        new_hour = "0" + new_hour


current()

