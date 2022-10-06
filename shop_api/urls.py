from django.urls import path, include, re_path
from .views import BooksApiList, CommentApiList, RatingApiList, AuthorsApiList

urlpatterns = [
   path('books/', BooksApiList.as_view()),
   path('authors/', AuthorsApiList.as_view()),
   path('comments/', CommentApiList.as_view()),
   path('ratings/', RatingApiList.as_view()),
]