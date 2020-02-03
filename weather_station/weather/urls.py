from django.urls import path
from .views import (
    get_forecast_search,
    get_cities_by_query,
    get_cities_by_coordinate,
    get_forecast
)

urlpatterns = [
    path(r"", get_forecast_search),
    path(r"query/", get_cities_by_query, name='query_view'),
    path(r"coordinates/", get_cities_by_coordinate, name='coordinate_view'),
    path(r"forecast/<int:city_id>", get_forecast),
]