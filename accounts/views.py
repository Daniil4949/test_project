from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from .forms import LoginUserForm, RegistrationForm
from users.models import *


class RegisterUser(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('home')
    template_name = "registration/registration.html"

# Create your views here.
