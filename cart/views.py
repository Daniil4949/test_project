from django.shortcuts import render, redirect
from books.models import Cart, Book
from .forms import SearchBookForm, PaymentForm
from .models import Payment
from django.shortcuts import get_object_or_404


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
    payment_form = PaymentForm(request.POST)
    books_in_cart = Cart.objects.filter(user=request.user)
    total_sum = get_total_sum(request)
    if request.method == 'POST':
        if payment_form.is_valid():
            for selected_book in books_in_cart:
                number_of_card = payment_form.cleaned_data['number_of_card']
                validity_period = payment_form.cleaned_data['validity_period']
                book = selected_book.book
                quantity_for_payment = selected_book.quantity
                book.quantity -= selected_book.quantity
                book.save()
                selected_book.delete()
                Payment.objects.create(number_of_card=payment_form.cleaned_data['number_of_card'],
                                       validity_period=payment_form.cleaned_data['validity_period'],
                                       purchased_book=book, quantity=quantity_for_payment)
            return redirect('home')
        return render(request, 'cart/payment.html', {'total_sum': total_sum, 'payment_form': payment_form})
    return render(request, 'cart/payment.html', {'total_sum': total_sum, 'payment_form': payment_form})


def get_total_sum(request):
    result = 0
    books_in_cart = Cart.objects.filter(user=request.user)
    for book in books_in_cart:
        result += book.quantity * book.book.price
    return result


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


def check_the_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    problem_books = []
    for book in cart:
        if book.quantity > book.book.quantity:
            problem_books.append(book)
    if problem_books:
        return render(request, "cart/fix_cart.html", {'books': problem_books})
    return redirect('payment')

# Create your views here.
