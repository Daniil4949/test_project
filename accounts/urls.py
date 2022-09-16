from django.urls import path, include
from .views import RegisterUser


urlpatterns = [
    path('registration/', RegisterUser.as_view(), name="registration"),

]
