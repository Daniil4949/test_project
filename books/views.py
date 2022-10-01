from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Category, Book, Author, Rating
from django.views import View
from django.views.generic.base import TemplateView

"""TODO:
    1. Improve design
    2. Refactoring the code in books/views.py
    Desired: 
    1. Add comments
    2. Add User's profile
"""


class MainPage(ListView):
    """There are 4 books for each page."""
    paginate_by = 4
    model = Book
    template_name = "menu/main_page.html"


class Authors(ListView):
    """There are 4 authors for each page."""
    paginate_by = 4
    model = Author
    template_name = 'menu/authors.html'


class CategoryBook(ListView):
    """There are all the books of the selected category"""
    template_name = "menu/category_books_page.html"
    model = Book
    context_object_name = 'books'
    allow_empty = False

    def get_queryset(self):
        """Getting all the books of the selected category with slug"""
        category = Category.objects.get(slug=self.kwargs['category_slug'])
        return Book.objects.filter(category=category)


class BookInfo(View):
    """Page for the selected book"""
    template_name = "menu/book.html"
    model = Book
    context_object_name = 'book'
    slug_url_kwarg = 'book_slug'
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        book_get = Book.objects.get(slug=self.kwargs['book_slug'])
        if request.user.is_authenticated:
            try:
                rating = Rating.objects.get(user=self.request.user, book=book_get)
            except Exception as e:
                Rating.objects.create(user=self.request.user, book=book_get)
                rating = Rating.objects.get(user=self.request.user, book=book_get)
            return render(request, 'menu/book.html', {'book': book_get, 'rating': rating})
        return render(request, 'menu/book.html', {'book': book_get})

    def post(self, request, *args, **kwargs):
        book_post = Book.objects.get(slug=self.kwargs['book_slug'])

        if request.user.is_authenticated:
            try:
                rating = Rating.objects.get(user=self.request.user, book=book_post)
            except Exception as e:
                Rating.objects.create(user=self.request.user, book=book_post)
                rating = Rating.objects.get(user=self.request.user, book=book_post)
            return render(request, 'menu/book.html', {'book': book_post, 'rating': rating})
        return render(request, 'menu/book.html', {'book': book_post})


class AuthorInfo(DetailView):
    """Page for the selected author"""
    template_name = "menu/author.html"
    model = Author
    context_object_name = 'author'
    slug_url_kwarg = 'author_slug'

# Create your views here.
