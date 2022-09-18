from django.contrib import admin
from django.urls import path, include
from .views import MainPage, BookInfo, CategoryBook, CartInfo


urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('categories/<slug:category_slug>/', CategoryBook.as_view(), name='category_books'),
    path('cart/<str:username>', CartInfo.as_view(), name='cart'),
    path('books/<slug:book_slug>/', BookInfo.as_view(), name='book')
]