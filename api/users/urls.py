from django.urls import path
from .views import UserLogin, UserRegistration, TokenRefresh, SwaggerView
from .utils.password_checks import PasswordChecker

UserRegistration.pass_checker = PasswordChecker()

urlpatterns = [
    path('users/login', UserLogin.as_view(), name='UserLogin'),
    path('users/signup', UserRegistration.as_view(),name='UserRegistration'),
    path('users/refresh-token', TokenRefresh.as_view(), name='TokenRefresh'),
    path('swagger', SwaggerView.as_view(), name='SwaggerView')
]