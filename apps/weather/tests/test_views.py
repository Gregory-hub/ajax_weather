from django.test import TestCase
from django.test import Client
from django.urls import reverse

class AjaxTestCase(TestCase):
    def test_return_json(self):
        response = self.client.get(reverse('weather:ajax'), {'qwerty': 'ytrewq'})
        print(type(response))
