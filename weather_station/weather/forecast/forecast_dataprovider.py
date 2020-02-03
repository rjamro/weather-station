from typing import List, Dict

class ForecastDataProvider(object):
    def __init__(self, data_provider):
        self.__data_provider = data_provider

    def get_cities_by_query(self, query: str) -> List[Dict]:
        return self.__data_provider.get_cities_by_query(query)

    def get_cities_by_coordinates(self, lattitude: float, longitude: float) -> List[Dict]:
        return self.__data_provider.get_cities_by_coordinates(lattitude, longitude)

    def get_forecast_data(self, city_id: int) -> Dict:
        return self.__data_provider.get_forecast_data(city_id)

    def get_weather_icon_path(self) -> str:
        return self.__data_provider.get_weather_icon_path()
