from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CoordinateForm, CityForm

# Create your views here.

def get_forecast(request, city_id):
    context = {}
    return render(request, "forecast_list.html", context=context)

def get_forecast_detail(request):
    context = {}
    return render(request, "forecast_detail.html", context=context)

def get_forecast_search(request):
    coordinate_form = CoordinateForm()
    city_form = CityForm()
    context = {
        "city_form": city_form,
        "coordinate_form": coordinate_form
    }

    return render(request, "forecast_form.html", context=context)

def get_cities_by_coordinate(request):
    context = {}
    return render(request, 'forecast_cities.html', context=context)

def get_cities_by_query(request):
    context = {}
    return render(request, 'forecast_cities.html', context=context)


