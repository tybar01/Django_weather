from django.urls import path
from . import views

urlpatterns = [
    path('', views.weatherapp),
    path('weather/', views.weather, name='weather')
]