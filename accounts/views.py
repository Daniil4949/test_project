from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import LoginUserForm, RegistrationForm
from users.models import *
from django.views import View


class RegisterUser(CreateView):
    """View class for the registration"""
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = "registration/registration.html"


class LoginUser(LoginView):
    """View class for the authentication"""
    form_class = LoginUserForm
    template_name = "registration/login.html"
    model = CustomUser
    success_url = reverse_lazy('home')


class Profile(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'menu/profile.html')
# Create your views here.
