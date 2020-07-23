import requests
import json

from django.test import TestCase
from django.test import Client
from django.conf import settings

from apps.weather.services import *


class CapitalizeCityNameTestCase(TestCase):
    def test_single_word_name(self):
        city_name = 'london'
        capitalized = capitalize_city_name(city_name)
        self.assertEquals(capitalized, 'London')


    def test_double_word_name(self):
        city_name = 'san francisco'
        capitalized = capitalize_city_name(city_name)
        self.assertEquals(capitalized, 'San Francisco')


    def test_is_none_passed(self):
        city_name = None
        capitalized = capitalize_city_name(city_name)
        self.assertEquals(capitalized, None)


class GetCityIdTestCase(TestCase):
    def setUp(self):
        self.city = City.objects.get_or_create(name="London", city_id=2643743)
        self.valid_id = 2643743


    def test_if_returns_valid_id(self):
        city_name = 'London'
        id = get_city_id(city_name)

        self.assertEquals(id, self.valid_id)


    def test_if_returns_valid_id_with_uncapitalized_city_name(self):
        city_name = 'london'
        id = get_city_id(city_name)

        self.assertEquals(id, self.valid_id)


    def test_if_none_passed(self):
        city_name = None
        id = get_city_id(city_name)
        self.assertEquals(id, None)


    def test_if_unexisting_city_name_passed(self):
        city_name = 'Burejuy'
        id = get_city_id(city_name)
        self.assertEquals(id, None)


class GetTemperatureTestCase(TestCase):
    def setUp(self):
        self.city = City.objects.get_or_create(name="London", city_id=2643743)
        self.valid_id = 2643743
        self.token = settings.OPEN_WEATHER_MAP_API_TOKEN


    def test_if_none_passed(self):
        city_name = None
        temperature = get_temperature(city_name)

        self.assertEquals(temperature, None)


    def test_if_unexisting_city_name_passed(self):
        city_name = 'Benjomen'
        temperature = get_temperature(city_name)

        self.assertEquals(temperature, None)


    def test_if_returns_valid_temperature(self):
        """You probably should run this twice(temperature can change while test is running)"""
        city_name = 'London'
        temperature = get_temperature(city_name)

        response = requests.get('http://api.openweathermap.org/data/2.5/weather?id={0}&appid={1}'.format(self.valid_id, self.token))
        valid_temperature = round(json.loads(response.text).get('main').get('temp') - 273.15, 1)

        self.assertEquals(temperature, valid_temperature)


    def test_if_returns_valid_temperature_with_uncapitalized_city_name(self):
        """You probably should run this twice(temperature can change while test is running)"""
        city_name = 'london'
        temperature = get_temperature(city_name)

        response = requests.get('http://api.openweathermap.org/data/2.5/weather?id={0}&appid={1}'.format(self.valid_id, self.token))
        valid_temperature = round(json.loads(response.text).get('main').get('temp') - 273.15, 1)

        self.assertEquals(temperature, valid_temperature)
