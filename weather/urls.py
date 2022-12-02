from django.urls import path
from weather.views import (
    WeatherView,
    CitiesView,
    CitiesListView,
    WeatherDayView,
    WeatherHoursListView,
    WeatherHoursView
)

urlpatterns = [
    path("cities/weather-status/<slug:city>/", WeatherView.as_view(), name="weather"),
    path("cities/weather-status/<slug:city>/<str:day>/", WeatherDayView.as_view(), name="weather-day"),
    path("cities/", CitiesListView.as_view(), name="cities-list"),
    path("cities/<slug:slug>/", CitiesView.as_view(), name="city"),
    path("cities/weather-status/<slug:city>/<str:day>/hours-list/", WeatherHoursListView.as_view(),
         name="day-hours-list"),
    path("cities/weather-status/<slug:city>/<str:day>/hours-list/<int:day_hours>/", WeatherHoursView.as_view(),
         name="day-hours"),
]
