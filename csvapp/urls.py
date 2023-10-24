from django.contrib import admin
from django.urls import path
from csvapp.views import home


urlpatterns = [
    path('home/', home),
]
