from django.contrib import admin
from weather.models import (
    City,
    Day,
    Hours
)

admin.site.register(City)


class HoursInline(admin.TabularInline):
    model = Hours


@admin.register(Day)
class WeatherAdmin(admin.ModelAdmin):
    inlines = [
        HoursInline,
    ]
