import requests

from typing import Dict, List
from rest_framework import serializers
from .serializers import ForecastSerializer, CitySerializer

class MetaWeatherDataProvider(object):
    __icon_path = "https://www.metaweather.com/static/img/weather/png/"

    def get_cities_by_query(self, query: str) -> List[Dict]:
        response = requests.get(
            f"https://www.metaweather.com/api/location/search/?query={query}",
            timeout=(3.5, 10)
        )
        return self._validate(response, CitySerializer, many=True)

    def get_cities_by_coordinates(self, lattitude: float, longitude: float) -> List[Dict]:
        response = requests.get(
            f"https://www.metaweather.com/api/location/search/?lattlong={lattitude},{longitude}",
            timeout=(3.5, 10)
        )
        return self._validate(response, CitySerializer, many=True)

    def get_forecast_data(self, city_id: int) -> Dict:
        response = requests.get(
            f"https://www.metaweather.com/api/location/{city_id}",
            timeout=(3.5, 10)
        )
        return self._validate(response, ForecastSerializer)

    def get_weather_icon_path(self) -> str:
        return self.__icon_path

    def _validate(
            self,
            response: requests.Response,
            serializer: serializers.Serializer,
            many: bool = False
        ) -> Dict:
        data = None
        if response.status_code == 200:
            data = response.json()
            serial_obj = serializer(data=data, many=many)
            if serial_obj.is_valid():
                data = serial_obj.validated_data
            else:
                raise serializers.ValidationError("Data is not compatible with the serializer.")
        else:
            raise serializers.ValidationError(f"Wrong status code: {response.status_code}")

        return data
