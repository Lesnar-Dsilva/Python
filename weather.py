import requests;#web requests
from pprint import pprint;#parse JSON

key = "f3b4ddef37f73517773672b92135a94d";
city = input("Enter a city: ");
api = f"https://api.openweathermap.org/data/2.5/weather?appid={key}&q={city}";
weather_data = requests.get(api).json();
pprint(weather_data["main"]);
#28mins 27/05/2022