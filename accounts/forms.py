from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from users.models import *


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }

    def clean_password2(self) -> str:
        data = self.cleaned_data
        if data['password1'] != data['password2']:
            raise forms.ValidationError("Passwords didn't match!")
        return data['password2']


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'password': forms.PasswordInput(attrs={'class': 'form-input'}),
        }

    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class': 'form-input'})),
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-input'})),
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
