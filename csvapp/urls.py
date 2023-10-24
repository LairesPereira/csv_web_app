from django.contrib import admin
from django.urls import path
from csvapp.views import home, teste

urlpatterns = [
    path('home/', home),
    path('home/teste/', teste)
]
