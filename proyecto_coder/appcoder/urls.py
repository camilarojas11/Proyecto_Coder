from operator import index
from django.urls import path
from appcoder.views import *


urlpatterns = [
    path('', index),
]
