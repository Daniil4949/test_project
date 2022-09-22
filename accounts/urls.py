from django.urls import path, include
from .views import RegisterUser, LoginUser, logout

urlpatterns = [
    path('registration/', RegisterUser.as_view(), name="registration"),
    path('login/', LoginUser.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),

]
