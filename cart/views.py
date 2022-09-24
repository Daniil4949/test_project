from django.shortcuts import render, redirect
from books.models import Cart, Book
from .forms import SearchBookForm

#TODO: It is necessary to implement search function

def cart(request):
    cart = Cart.objects.filter(user=request.user)
    return render(request, "cart/cart.html", {"cart": cart})


def add_to_cart(request, book_slug):
    try:
        book = Book.objects.get(slug=book_slug)
        cart = Cart.objects.get(user=request.user, book=book)
        cart.quantity += 1
        cart.save()
    except:
        book = Book.objects.get(slug=book_slug)
        Cart.objects.create(user=request.user, book=book)
    return redirect("home")


def delete_from_the_cart(request, book_slug):
    book = Book.objects.get(slug=book_slug)
    delete_list = Cart.objects.filter(user=request.user, book=book)
    delete_list.delete()
    return redirect('cart')


def delete_all(request):
    delete_list = Cart.objects.filter(user=request.user)
    delete_list.delete()
    return redirect('cart')


def payment(request):
    return render(request, 'cart/payment.html')

# def search_book(request):
#     """Form for searching books"""
#     search_form = SearchBookForm(request.POST)
#     if request.method == 'POST':
#         if search_form.is_valid():
#             title = search_form.cleaned_data['title']
#             books = Book.objects.filter(title__contains=str(title))
#             return render(request, 'menu/category_books.html', {'books': books})
#         return render(request, 'menu/category_books.html', {'books': books})
#     return redirect('home')

# Create your views here.
