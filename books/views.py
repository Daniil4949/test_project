from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
    return render(request, "menu/main_page.html")
# Create your views here.
