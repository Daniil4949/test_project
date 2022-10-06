from django.urls import path, include, re_path
from .views import (BooksApiList, CommentApiList, RatingApiList,
                    AuthorsApiList, CommentApiUpdate, RatingApiUpdate, BooksApiUpdate,
                    AuthorApiUpdate)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('books/', BooksApiList.as_view()),
    path('authors/', AuthorsApiList.as_view()),
    path('comments/', CommentApiList.as_view()),
    path('ratings/', RatingApiList.as_view()),
    path('comments/<int:pk>/', CommentApiUpdate.as_view()),
    path('books/<int:pk>/', BooksApiUpdate.as_view()),
    path('ratings/<int:pk>/', RatingApiUpdate.as_view()),
    path('authors/<int:pk>/', AuthorApiUpdate.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
