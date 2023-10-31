from django.contrib import admin
from django.urls import path
from csvapp.views import home, name_to_filter

urlpatterns = [
    path('', home),
    path('name_to_filter/', name_to_filter)
]
