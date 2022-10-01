from django.contrib import admin
from django.urls import path, include
from .views import MainPage, BookInfo, CategoryBook, Authors, AuthorInfo


urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('categories/<slug:category_slug>/', CategoryBook.as_view(), name='category_books'),
    path('books/<slug:book_slug>/', BookInfo.as_view(), name='book'),
    path('authors/', Authors.as_view(), name='authors'),
    path('author/<slug:author_slug>/', AuthorInfo.as_view(), name='author'),

]