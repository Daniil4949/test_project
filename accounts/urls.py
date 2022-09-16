from django.urls import path, include
from .views import RegisterUser, LoginUser


urlpatterns = [
    path('registration/', RegisterUser.as_view(), name="registration"),
    path('login/', LoginUser.as_view(), name='login')

]
