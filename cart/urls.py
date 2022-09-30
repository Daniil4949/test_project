from django.urls import path, include
from .views import *

urlpatterns = [
    path('', cart, name='cart'),
    path('add_to_cart/<slug:book_slug>/', add_to_cart, name='add_to_cart'),
    path('delete_from_the_cart/<slug:book_slug>/', delete_from_the_cart, name='delete_from_the_cart'),
    path('delete_all/', delete_all, name='delete_all'),
    path('payment/', payment, name='payment'),
    path('search_book/', search_book, name='search_book'),
    path('check_the_cart/', check_the_cart, name='check_the_cart'),
    path('payment/', payment, name='payment'),
]
