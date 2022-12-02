from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

Weather_STATUS = (
    ("Sunny", "Sunny"),
    ("Partially cloudy", "Partially cloudy"),
    ("Cloudy", "Cloudy"),
    ("Overcast", "Overcast"),
    ("Rainy", "Rainy"),
    ("Drizzle", "Drizzle"),
    ("Snowy", "Snowy"),
    ("Stormy", "Stormy"),
    ("Tornadoes", "Tornadoes"),
    ("Thundersnow", "Thundersnow"),
    ("Thunderstorm", "Thunderstorm"),
    ("Fog", "Fog"),
    ("Hurricanes", "Hurricanes"),
    ("Sandstorms", "Sandstorms")
)

Days_Of_Week = (
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday"),
)

Days_In_URL = (
    ("monday", "monday"),
    ("tuesday", "tuesday"),
    ("wednesday", "wednesday"),
    ("thursday", "thursday"),
    ("friday", "friday"),
    ("saturday", "saturday"),
    ("sunday", "sunday"),
)


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("City"))
    slug = models.SlugField(
        max_length=255,
        verbose_name=_("Name in URL"),
        unique=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")


class Day(models.Model):
    day = models.CharField(choices=Days_Of_Week, verbose_name=_("Day"), max_length=88)
    date = models.DateTimeField(default=timezone.now(), verbose_name=_("Date"))
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name=_("City"))
    status = models.CharField(choices=Weather_STATUS, verbose_name=_("Weather status"), max_length=88)
    temperature = models.IntegerField(verbose_name=_("Temperature"))

    def __str__(self):
        return self.day

    class Meta:
        verbose_name = _("Day")
        verbose_name_plural = _("Days")


class Hours(models.Model):
    this_hour_status = models.CharField(choices=Weather_STATUS, verbose_name=_("This hour status"), max_length=88)
    day = models.ForeignKey(
        Day,
        on_delete=models.CASCADE,
        related_name="weather_hours",
        verbose_name=_("The weather status of today")
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name=_("City"),
    )
    day_hours = models.IntegerField(verbose_name=_("Hour"))
    temperature = models.IntegerField(verbose_name=_("Temperature of this hour"))

    class Meta:
        verbose_name = _("Hour")
        verbose_name_plural = _("Hours")
