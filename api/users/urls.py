from django.urls import path
from .views import UserLogin, UserRegistration

urlpatterns = [
     path('users/login', UserLogin.as_view(), name='UserRegistration'),
     path('users/signup', UserRegistration.as_view(), name='UserLogin')
]
   