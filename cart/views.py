from django.shortcuts import render
from books.models import Cart


def cart(request):
    cart = Cart.objects.filter(user=request.user)
    return render(request, "cart/cart.html", {"cart": cart})

# Create your views here.
