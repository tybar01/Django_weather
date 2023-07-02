# Overview

This project was intended as a way to understand wep apps and api calls using django in python.

This webapp lets you enter the name of a city and get back the weather for that city using open weather api

To start the server you open a terminal in the django folder and type the command "python manage.py runserver" 

After that you copy and paste the http adreses and add "playground/" to enter the app. 

The purpose for writing this program was to allow for a basic understanding of backend programming for web apps. It was not intended as a full
front end experience, but more of how to handle requests from the user. 

[Software Demo Video](https://youtu.be/blxNyI_W8RI)

# Web Pages

The intro page:

Used to enter the program and take user input.

Once the user hits submit they are taken to the results or the error page

The results page:

Takes the response from the first page and outputs a city, weather, and temp.

It also allows for another user input which can send the user back to
results page for another city, or to the error page. 

The error page: 

This page takes the city name that the user entered before and displays it
as well as prompts the user for another input. 

# Development Environment

The main 2 tools used in here are django and openweather

Django is used for creating a virtual environment to allow the web app to run as well as
provides a framework for the apps that we use in a python environment. 

Openweather allows for a an API call that can return a large amount of weather
data to be used based on inputs such as city name, latitude longitude, or zip code.

The language I Used was python due to the experience I have with it and the vast 
amounts of documentation and tutortials. It's a runtime environment which lends
well to fast attempts at running the code.

The library i used was requests which is used for making api calls.

# Useful Websites
* [Basic Django tutorial](https://www.youtube.com/watch?v=OTmQOjsl0eg&ab_channel=Telusko)
* [Weather API tutorial](https://youtu.be/9P5MY_2i7K8)

# Future Work
* More robust error handling (fix the empty set)
* Format front end for a more veritcal output
* Allow user to select paramaters to display.
