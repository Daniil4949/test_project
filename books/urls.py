from django.contrib import admin
from django.urls import path, include
from .views import MainPage, BookInfo


urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    # path('<slug:category_slug>/', CategoryBook.as_view(), name='category_books'),
    # path('cart/', Cart.as_view(), name='cart'),
    path('<slug:book_slug>/', BookInfo.as_view(), name='book')
]