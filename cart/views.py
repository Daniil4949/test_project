from django.shortcuts import render, redirect
from books.models import Cart, Book
from .forms import SearchBookForm


def cart(request):
    """Returns all the products and it's quantity for each user"""
    cart = Cart.objects.filter(user=request.user)
    return render(request, "cart/cart.html", {"cart": cart})


def add_to_cart(request, book_slug):
    """Block try/except is necessary because we try to find book firstly, and after that
    we add the selected book to the cart or increase books' quantity. if we do not use block try/except
    it would not work in a correct way because we cannot find book that does not exist. We can use 'get_object_or_404'
    instead.' """
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
    """Deleting the definite book from the cart"""
    book = Book.objects.get(slug=book_slug)
    delete_list = Cart.objects.filter(user=request.user, book=book)
    delete_list.delete()
    return redirect('cart')


def delete_all(request):
    """Deleting all the books from the cart"""
    delete_list = Cart.objects.filter(user=request.user)
    delete_list.delete()
    return redirect('cart')


def payment(request):
    return render(request, 'cart/payment.html')


def search_book(request):
    """Form for searching books. It is working also with not the full title of the book."""
    search_form = SearchBookForm(request.POST)
    if request.method == 'POST':
        if search_form.is_valid():
            title = search_form.cleaned_data['title']
            books = Book.objects.filter(title__contains=str(title))
            return render(request, 'menu/category_books_page.html', {'books': books})
        return render(request, 'menu/category_books_page.html')
    return redirect('home')

# Create your views here.
