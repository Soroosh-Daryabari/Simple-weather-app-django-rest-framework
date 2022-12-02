from weather.models import City, Day, Hours
from rest_framework import serializers


class HoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hours
        fields = ("this_hour_status", "day_hours", "temperature", "city")


class WeatherSerializer(serializers.ModelSerializer):
    weather_hours = HoursSerializer(many=True)

    class Meta:
        model = Day
        fields = (
            "day",
            "date",
            "status",
            "temperature",
            "weather_hours",
        )
        ordering = ("-date",)


class CitySerializer(serializers.ModelSerializer):
    weather = WeatherSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ("name", "slug", "weather")
