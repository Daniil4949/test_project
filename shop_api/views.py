from rest_framework import generics
from cart.models import Cart, Payment
from books.models import Book, Rating, Author, Category, Comment
from rest_framework.permissions import IsAuthenticated
from .serializers import BookSerializer, AuthorSerializer, RatingSerializer, CategorySerializer, CommentSerializer


class BooksApiList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorsApiList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CommentApiList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class RatingApiList(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer



# Create your views here.
