from django.shortcuts import render
import requests
import os
from dotenv import dotenv_values
from .form import SearchForm


def weatherapp_api(request):
    OPEN_WEATHER_API_KEY = dotenv_values(os.getcwd() + "/weatherappapi/.env")["OPEN_WEATHER_API_KEY"]
    OPEN_WEATHER_API_URL = dotenv_values(os.getcwd() + "/weatherappapi/.env")["OPEN_WEATHER_API_URL"]
    form = SearchForm()
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            try: # catching any key error
                city = form.cleaned_data['search_bar'] # search value entered
                BASE_URL = OPEN_WEATHER_API_URL + city + "&appid=" + OPEN_WEATHER_API_KEY
                
                coordinates = requests.get(BASE_URL).json()['coord']
                wind = requests.get(BASE_URL).json()['wind']
                data_stats = requests.get(BASE_URL).json()['main']
                other_data = requests.get(BASE_URL).json()['sys']
                clouds_status = requests.get(BASE_URL).json()['weather'][0]
                temp = round(data_stats['temp'] - 273.15, 2)
                feels_like = round(data_stats['feels_like'] - 273.15, 2)
                temp_min = round(data_stats['temp_min'] - 273.15, 2)
                temp_max = round(data_stats['temp_max'] - 273.15, 2)
                pressure = data_stats['pressure']
                humidity = data_stats['humidity']
                country = other_data['country']
                city = requests.get(BASE_URL).json()['name']
                clouds = clouds_status['description']

                context = {
                    "form":form,
                    "wind":wind,
                    "coordinates":coordinates,
                    "temp":temp,
                    "feels_like":feels_like,
                    "temp_min":temp_min,
                    "temp_max":temp_max,
                    "pressure":pressure,
                    "humidity":humidity,
                    "country":country,
                    "city":city,
                    "clouds":clouds,
                    }
                return render(request, "weatherappapi/index.html", context)
            except KeyError as e:
                print("Enter a valid city name")

            
        
    return render(request, "weatherappapi/index.html", {"form":form})


