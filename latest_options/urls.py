from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.latest_options, name='latest_options'),
]
