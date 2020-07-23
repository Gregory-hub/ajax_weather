from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import *
from .services import *

def index(request):
    template = 'weather/index.html'

    return render(request, template)


def ajax(request):
    city = request.GET.get('request_city', default=None)
    if city == '':
        city = None

    temperature = get_temperature(city)

    if temperature == None:
        json_response = {
            'city': None,
            'temperature': None
        }

    else:
        json_response = {
            'city': capitalize_city_name(city),
            'temperature': temperature
        }

    return JsonResponse(json_response)
