from .views import *
from django.urls import path

urlpatterns = [
    path('', main),
    path('about', about),
]