from django.test import TestCase
from django.urls import reverse

class WeatherViewTest(TestCase):
    # weather view
    def test_weatherview_url_exists_at_desired_location(self):
        response = self.client.get('/weather/')
        self.assertEqual(response.status_code, 200)

    def test_weatherview_uses_correct_template(self):
        response = self.client.get('/weather/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forecast_form.html')

    # query view
    def test_queryview_url_exists_at_desired_location(self):
        response = self.client.get('/weather/query/')
        self.assertEqual(response.status_code, 200)

    def test_queryview_is_accessible_by_name(self):
        response = self.client.get(reverse('query_view'))
        self.assertEqual(response.status_code, 200)

    def test_queryview_uses_correct_template(self):
        response = self.client.get('/weather/query/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forecast_cities.html')

    # coordinate view
    def test_coordinatesview_url_exists_at_desired_location(self):
        response = self.client.get('/weather/coordinates/')
        self.assertEqual(response.status_code, 200)

    def test_coordinatesview_is_accessible_by_name(self):
        response = self.client.get(reverse('coordinate_view'))
        self.assertEqual(response.status_code, 200)

    def test_coordinatesview_uses_correct_template(self):
        response = self.client.get('/weather/coordinates/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forecast_cities.html')

    # forecast view
    def test_forecastview_url_exists_at_desired_location(self):
        response = self.client.get('/weather/forecast/1')
        self.assertEqual(response.status_code, 200)

    def test_forecastview_uses_correct_template(self):
        response = self.client.get('/weather/forecast/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forecast_list.html')
