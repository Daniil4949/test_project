from django.shortcuts import render, redirect
from books.models import Cart, Book


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

# Create your views here.
