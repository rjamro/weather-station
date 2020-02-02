from django.test import TestCase
from unittest import mock
from django.urls import reverse
from ..forecast.serializers import CitySerializer
from ..forecast import MetaWeatherDataProvider
from rest_framework.serializers import ValidationError
import requests

class MetaWeatherDataProviderTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.data_provider = MetaWeatherDataProvider()
    
    def setUp(self):
        self.response = mock.MagicMock(spec=requests.Response)

    def test_validate_with_correct_data(self):
        self.response.json.return_value = {
            "woeid": 1,
            "title": 2
        }
        self.response.status_code = 200
        result = self.data_provider._validate(self.response, CitySerializer)
        self.assertEqual(result['woeid'], 1)

    def test_validate_with_incorrect_data(self):
        self.response.json.return_value = {
            "nonexistingfield": 1,
            "title": 2
        }
        self.response.status_code = 200
        with self.assertRaises(ValidationError):
            result = self.data_provider._validate(self.response, CitySerializer)
    
    def test_validate_with_error_status_code(self):
        self.response.json.return_value = {
            "woeid": 1,
            "title": 2
        }
        self.response.status_code = 400
        with self.assertRaises(ValidationError):
            result = self.data_provider._validate(self.response, CitySerializer)

    def test_validate_with_list_in_response(self):
        self.response.json.return_value = [
            {
                "woeid": 1,
                "title": 2
            },
            {
                "woeid": 2,
                "title": 5
            }
        ]
        self.response.status_code = 200
        result = self.data_provider._validate(self.response, CitySerializer, many=True)
        self.assertEqual(len(result), 2)

    def test_validate_with_empty_object_in_response(self):
        self.response.json.return_value = {}
        self.response.status_code = 200
        with self.assertRaises(ValidationError):
            result = self.data_provider._validate(self.response, CitySerializer)

    def test_validate_with_empty_list_in_response(self):
        self.response.json.return_value = []
        self.response.status_code = 200
        result = self.data_provider._validate(self.response, CitySerializer, many=True)
        self.assertEqual(result, [])



