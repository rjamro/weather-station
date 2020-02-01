from django import forms

class CoordinateForm(forms.Form):
    lattitude = forms.FloatField(label="Lattitude")
    longitude = forms.FloatField(label="Longitude")

class CityForm(forms.Form):
    query = forms.CharField(max_length=100, label="City name")

