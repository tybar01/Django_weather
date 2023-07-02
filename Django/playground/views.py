from django.shortcuts import render
import requests
from django.http import HttpResponse




def weatherapp(request):
    return render(request, 'home.html')

def weather(request):

    city = request.GET['city']

    api_key = 'abe41c8336590311449d3c2565019da8'

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")


    if weather_data.json()['cod'] == '404':
        return render(request, 'weather_error.html', {'city': city} )
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = weather_data.json()['main']['temp']

        return render(request, 'result.html', {'city': city, 'weather' : weather, 'temp' : temp} )

