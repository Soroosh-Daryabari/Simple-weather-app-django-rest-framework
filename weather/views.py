from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from weather.models import Day, Hours
from weather.serializers import WeatherSerializer, CitySerializer, HoursSerializer
from weather.permissions import IsStaffOrReadOnly
from weather.models import City


class CitiesListView(ListCreateAPIView):
    serializer_class = CitySerializer
    permission_classes = (IsStaffOrReadOnly,)
    queryset = City.objects.all()


class CitiesView(RetrieveUpdateDestroyAPIView):
    serializer_class = CitySerializer
    permission_classes = (IsStaffOrReadOnly,)
    queryset = City.objects.all()
    lookup_field = "slug"


class WeatherView(ListCreateAPIView):
    serializer_class = WeatherSerializer
    permission_classes = (IsStaffOrReadOnly,)

    def get_queryset(self):
        return Day.objects.filter(city__slug=self.kwargs.get("city"))


class WeatherDayView(RetrieveUpdateDestroyAPIView):
    serializer_class = WeatherSerializer
    permission_classes = (IsStaffOrReadOnly,)
    lookup_field = "day"

    def get_queryset(self):
        return Day.objects.filter(city__slug=self.kwargs.get("city"))


class WeatherHoursListView(ListCreateAPIView):
    serializer_class = HoursSerializer
    permission_classes = (IsStaffOrReadOnly,)

    def get_queryset(self):
        return Hours.objects.filter(
            city__slug=self.kwargs.get("city"),
            day__day=self.kwargs.get("day")
        )


class WeatherHoursView(RetrieveUpdateDestroyAPIView):
    serializer_class = HoursSerializer
    permission_classes = (IsStaffOrReadOnly,)
    lookup_field = "day_hours"

    def get_queryset(self):
        return Hours.objects.filter(
            city__slug=self.kwargs.get("city"),
            day__day=self.kwargs.get("day")
        )
