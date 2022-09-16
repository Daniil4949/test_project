from django.contrib import admin
from django.urls import path, include
from .views import main_page, MainPage


urlpatterns = [
    path('', MainPage.as_view(), name='home'),
]