from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Category, Book


#TODO: create all the classes for the cayegories and make it work in a right way


class MainPage(ListView):
    model = Book
    template_name = "menu/main_page.html"


class CategoryBook(DetailView):
    template_name = "menu/category_books_page.html"
    slug_url_kwarg = 'category_slug'
    context_object_name = 'books'

    def get_queryset(self):
        cat = self.kwargs['category_slug']
        category = Category.objects.get(slug=cat)
        return Book.objects.filter(category=category)


class Cart(DetailView):
    template_name = "menu/cart.html"

    def get_queryset(self):
        return Cart.objects.filter(user=self.kwargs['user'])

# Create your views here.
