from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Category, Book


def main_page(request):
    return render(request, "menu/main_page.html")


class MainPage(ListView):
    model = Book
    template_name = "menu/main_page.html"


# Create your views here.
