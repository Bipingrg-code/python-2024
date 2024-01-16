import requests
import json
import os

os.system(
    f"espeak 'Enter the city name where you want to know the current tempreture'")
city = input("City Name:")

api_URL = f"http://api.weatherapi.com/v1/current.json?key=83257312e7ab4947ac875135241601&q={city}"

req = requests.get(api_URL)

# parse to dictionary
data = json.loads(req.text)
# print(data)

# display the current tem_c
results = data["current"]["temp_c"]

# local time
time = data["location"]["localtime"]
os.system(f"espeak 'The current temp of {city} is {results}'")
os.system(f"espeak 'The local time of {city} is {time}'pokhara")
print(results)
