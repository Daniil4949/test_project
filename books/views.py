from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Book, Author, Rating


"""TODO:
    1. Improve design
    Desired: 
    1. Add comments
    2. Add User's profile
    3. Add ratings for the books
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


class BookInfo(DetailView):
    """Page for the selected book"""
    template_name = "menu/book.html"
    model = Book
    context_object_name = 'book'
    slug_url_kwarg = 'book_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            rating = Rating.objects.get(user=self.request.user, book__slug=self.kwargs['book_slug'])
            context['rating'] = rating
            return context
        except Exception as e:
            return context


def book_info(request, book_slug):
    book = Book.objects.get(slug=book_slug)
    try:
        rating = Rating.objects.get(user=request.user, book__slug=book_slug)
    except Exception as e:
        rating = ''
    return render(request, 'menu/book.html', {'book': book, 'rating': rating})


class AuthorInfo(DetailView):
    """Page for the selected author"""
    template_name = "menu/author.html"
    model = Author
    context_object_name = 'author'
    slug_url_kwarg = 'author_slug'

# Create your views here.
