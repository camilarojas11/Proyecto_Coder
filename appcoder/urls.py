from django.urls import path
from appcoder.views import *

urlpatterns = [
    path('', index, name= "home"),
]
