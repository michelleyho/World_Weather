import requests
import json

BASE_URL="https://api.openweathermap.org/data/2.5/weather?"
CITIES=["San Jose", "New York", "Philadelphia", "Austin", "Dallas", "Houston", "Seattle", "Paris", "Rome", "Munich"]
API_KEY=""

def get_weather(city):
    URL = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=imperial"
    response = requests.get(URL)
    
    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        temperature = main['temp']
        humidity = main["humidity"]
        pressure = main["pressure"]
        report = data['weather']
        
        print(f"{CITY:-^30}")
        print(f"Temperature: {temperature}F")
        print(f"Humidity: {humidity}")
        print(f"Pressure: {pressure}")
        print(f"Weather Report: {report[0]['description']}")
    else:
        print("Error in HTTP request")



for CITY in CITIES:
    get_weather(CITY)
