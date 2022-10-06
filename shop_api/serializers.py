from cart.models import Cart, Payment
from books.models import Book, Rating, Author, Category
from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = ('title', 'info', 'price', 'quantity', 'writer', 'category')


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = ('name', )


class AuthorSerializer(serializers.Serializer):
    class Meta:
        model = Author
        fields = ('name', 'info')


class CartSerializer(serializers.Serializer):
    class Meta:
        model = Cart
        fields = '__all__'


class RatingSerializer(serializers.Serializer):
    class Meta:
        model = Rating
        fields = "__all__"


class PaymentSerializer(serializers.Serializer):
    class Meta:
        model = Payment
        fields = ('number_of_card', 'validity_period', 'purchased_book', 'quantity')


