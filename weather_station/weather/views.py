from django.shortcuts import render, redirect
from django.http import HttpResponseServerError
from django.urls import reverse
from .forms import CoordinateForm, CityForm
from .forecast import ForecastDataProvider, MetaWeatherDataProvider
from rest_framework.serializers import ValidationError
# Create your views here.

data_provider = ForecastDataProvider(MetaWeatherDataProvider())

def get_forecast(request, city_id):
    try:
        forecast = data_provider.get_forecast_data(city_id=city_id)
    except ValidationError:
        return render(request, "forecast_validation_error.html")

    icon_url = data_provider.get_weather_icon_path()
    context = {
        "forecast": forecast,
        "icon_url": icon_url
    }
    return render(request, "forecast_list.html", context=context)

def get_forecast_detail(request):
    context = {}
    return render(request, "forecast_detail.html", context=context)

def get_forecast_search(request):
    if request.method == 'POST':
        if 'city_form' in request.POST:
            city_form = CityForm(request.POST)
            if city_form.is_valid():
                query = city_form.cleaned_data["query"]
                url = f'{reverse("query_view")}?text={query}'
                return redirect(url)
        elif 'coordinate_form' in request.POST:
            coordinate_form = CoordinateForm(request.POST)
            if coordinate_form.is_valid():
                longitude = coordinate_form.cleaned_data["longitude"]
                lattitude = coordinate_form.cleaned_data["lattitude"]
                url = f'{reverse("coordinate_view")}?long={longitude}&latt={lattitude}'
                return redirect(url)
    else:
        coordinate_form = CoordinateForm()
        city_form = CityForm()
        context = {
            "city_form": city_form,
            "coordinate_form": coordinate_form
        }

        return render(request, "forecast_form.html", context=context)

def get_cities_by_coordinate(request):
    lattitude = request.GET.get("latt", 0.0)
    longitude = request.GET.get("long", 0.0)
    try:
        cities = data_provider.get_cities_by_coordinates(
            lattitude=lattitude, 
            longitude=longitude
        )
    except ValidationError:
        return render(request, "forecast_validation_error.html")
        
    context = {"cities": cities}
    return render(request, 'forecast_cities.html', context=context)

def get_cities_by_query(request):
    query = request.GET.get("text", "Not specified")
    try:
        cities = data_provider.get_cities_by_query(query=query)
    except ValidationError:
        return render(request, "forecast_validation_error.html")

    context = {"cities": cities}
    return render(request, 'forecast_cities.html', context=context)


