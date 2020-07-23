from django.urls import path

from .views import *


app_name = 'weather'
urlpatterns = [
    path('', index, name='index'),
    path('ajax', ajax, name='ajax'),
]
