import json
import unittest

import json
import unittest

from django.test import TestCase
from django.test import Client
from django.urls import reverse

from apps.weather.models import City


class IndexViewTestCase(TestCase):
    def test_response_status(self):
        response = self.client.get(reverse('weather:index'))
        self.assertIs(response.status_code, 200)


class AjaxViewTestCase(TestCase):
    def setUp(self):
        self.city = City.objects.get_or_create(name="London", city_id=2643743)


    def test_response_status(self):
        response = self.client.get(reverse('weather:ajax'))
        self.assertIs(response.status_code, 200)

        response = self.client.get(reverse('weather:ajax'), {'request_city': 'London'})
        self.assertIs(response.status_code, 200)

        response = self.client.get(reverse('weather:ajax'), {'request_city': 'asdfggs'})
        self.assertIs(response.status_code, 200)

        response = self.client.get(reverse('weather:ajax'), {'request_city': 'London', 'qwerty': 'qwertyuio'})
        self.assertIs(response.status_code, 200)

        response = self.client.get(reverse('weather:ajax'), {'request_city': ''})
        self.assertIs(response.status_code, 200)


    def test_return_json(self):
        response = self.client.get(reverse('weather:ajax'), {'request_city': 'london'})
        content = json.loads(response.content)
        city = content['city']
        self.assertEquals(city, 'London')

        response = self.client.get(reverse('weather:ajax'), {'request_city': 'London'})
        content = json.loads(response.content)
        city = content['city']
        self.assertEquals(city, 'London')

        response = self.client.get(reverse('weather:ajax'), {'request_city': 'lond'})
        content = json.loads(response.content)
        city = content['city']
        self.assertEquals(city, None)
