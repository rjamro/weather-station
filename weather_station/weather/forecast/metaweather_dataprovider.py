import json
import requests
from typing import Dict, List
from .serializers import ForecastSerializer, CitySerializer
from rest_framework import serializers

class MetaWeatherDataProvider(object):
    def getCitiesByText(self, query: str) -> List[Dict]:
        response = requests.get(
            f"https://www.metaweather.com/api/location/search/?query={query}",
            timeout=(3.5, 10)
        )
        return self._validate(response, CitySerializer, many=True)

    def getCitiesByCoordinates(self, lattitude: float, longitude: float) -> List[Dict]:
        response = requests.get(
            f"https://www.metaweather.com/api/location/search/?lattlong={lattitude},{longitude}",
            timeout=(3.5, 10)
        )
        return self._validate(response, CitySerializer, many=True)

    def getForecastData(self, city_id: int) -> Dict:
        response = requests.get(
            f"https://www.metaweather.com/api/location/{city_id}",
            timeout=(3.5, 10)
        )
        return self._validate(response, ForecastSerializer)

    def getWeatherIconPath(self) -> str:
        return f"https://www.metaweather.com/static/img/weather/png/"

    def _validate(self, response: requests.Response, serializer: serializers.Serializer, many: bool = False) -> Dict:
        if response.status_code == 200:
            data = response.json()
            serial_obj = serializer(data=data, many=many)
            if serial_obj.is_valid():
                return serial_obj.validated_data
            else:
                raise serializers.ValidationError("Data is not compatible with the serializer.")
        else:
            raise 