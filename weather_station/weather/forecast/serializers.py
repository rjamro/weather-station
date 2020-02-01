from rest_framework import serializers

class DaySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    weather_state_name = serializers.CharField(max_length=100)
    weather_state_abbr = serializers.CharField(max_length=10)
    wind_direction_compass = serializers.CharField(max_length=100)
    applicable_date = serializers.CharField(max_length=100)
    min_temp = serializers.FloatField()
    max_temp = serializers.FloatField()
    the_temp = serializers.FloatField()
    wind_speed = serializers.FloatField()
    wind_direction = serializers.FloatField()
    air_pressure = serializers.FloatField()
    humidity = serializers.FloatField()
    visibility = serializers.FloatField()
    predictability = serializers.FloatField()

    def validate_the_temp(self, value):
        return round(value, 1)

class ForecastSerializer(serializers.Serializer):
    consolidated_weather = DaySerializer(many=True)
    time = serializers.CharField(max_length=100)
    sun_rise = serializers.CharField(max_length=100)
    sun_set = serializers.CharField(max_length=100)

class CitySerializer(serializers.Serializer):
    woeid = serializers.IntegerField()
    title = serializers.CharField(max_length=100)