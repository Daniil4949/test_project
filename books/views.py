from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Category, Book, Cart
from users.models import CustomUser


# TODO: create all the classes for the cayegories and make it work in a right way


class MainPage(ListView):
    model = Book
    template_name = "menu/main_page.html"


class CategoryBook(ListView):
    template_name = "menu/category_books_page.html"
    model = Book
    context_object_name = 'books'
    allow_empty = False

    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs['category_slug'])
        return Book.objects.filter(category=category)


class BookInfo(DetailView):
    template_name = "menu/book.html"
    model = Book
    context_object_name = 'book'
    slug_url_kwarg = 'book_slug'

# Create your views here.
