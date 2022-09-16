from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from .forms import LoginUserForm, RegistrationForm
from users.models import *
from django.contrib.auth.forms import AuthenticationForm


#TODO: Create appropriate classes for Authentication/Registration


class RegisterUser(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('home')
    template_name = "registration/registration.html"


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "registration/login.html"
    model = CustomUser
    success_url = reverse_lazy('home')
# Create your views here.
