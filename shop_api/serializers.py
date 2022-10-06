from cart.models import Cart, Payment
from books.models import Book, Rating, Author, Category, Comment
from rest_framework import serializers

"""
Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that 
can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, 
allowing parsed data to be converted back into complex types, after first validating the incoming data.
The serializers in REST framework work very similarly to Django's Form and ModelForm classes. We provide a 
Serializer class which gives you a powerful, generic way to control the output of your responses, as well as 
a ModelSerializer class which provides a useful shortcut for creating serializers that 
deal with model instances and querysets.
"""


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'info')


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('number_of_card', 'validity_period', 'purchased_book', 'quantity')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
