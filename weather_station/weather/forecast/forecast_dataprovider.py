from typing import List, Dict

class ForecastDataProvider(object):
    def __init__(self, data_provider):
        self.__data_provider = data_provider

    def getCitiesByQuery(self, query: str):
        return self.__data_provider.getCitiesByText(query)

    def getCitiesByCoordinates(self, lattitude: float, longitude: float):
        return self.__data_provider.getCitiesByCoordinates(lattitude, longitude)

    def getForecastData(self, city_id: int):
        return self.__data_provider.getForecastData(city_id)

    def getWeatherIconPath(self) -> str:
        return self.__data_provider.getWeatherIconPath()