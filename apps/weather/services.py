import requests
import json

from django.utils import timezone
from django.conf import settings

from .models import City


def capitalize_city_name(city_name):
    name_parts = [word.capitalize() for word in city_name.split(' ')]

    city_name = ' '.join(name_parts)

    return city_name



def get_city_id(city_name):

    city_name = capitalize_city_name(city_name)

    if City.objects.filter(name=city_name).exists():
        city_id = City.objects.filter(name=city_name)[0].city_id
    else:
        city_id = None
    return city_id


def get_temperature(city_name):
    if city_name == None:
        return None

    token = settings.OPEN_WEATHER_MAP_API_TOKEN

    city_id = get_city_id(city_name)

    if city_id == None:
        return None

    response = requests.get('http://api.openweathermap.org/data/2.5/weather?id={0}&appid={1}'.format(city_id, token))
    K_temp = json.loads(response.text)['main']['temp']
    temp = round(K_temp - 273.15, 1)

    return temp
