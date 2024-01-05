from django.urls import path
from .views import UserLogin, UserRegistration, TokenRefresh

urlpatterns = [
     path('users/login', UserLogin.as_view(), name='UserRegistration'),
     path('users/signup', UserRegistration.as_view(), name='UserLogin'),
     path('users/refresh-token', TokenRefresh.as_view(), name='TokenRefresh')
]