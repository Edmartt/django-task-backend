import json
import jwt
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views import View
from .utils.custom_jwt import create_jwt, create_refresh_token
from .utils.password_checks import PasswordChecker

#pass_checker_instance = PasswordChecker()

class UserRegistration(View):
    pass_checker = None
    
    def __init__(self):
        pass
    
    @method_decorator(require_http_methods(['POST']))
    def post(self, request):

        request_data = json.loads(request.body)
        username = request_data.get('username')
        password = request_data.get('password')
        compared_password = request_data.get('compared_password')

        if username and password and compared_password:
            if not self.pass_checker.check_password_length(password) and not self.pass_checker.check_password_length(compared_password):
                return JsonResponse({'response': 'password allowed minumun 8 character length'}, status=400)
            
            if not self.pass_checker.compare_password(password, compared_password):
                return JsonResponse({'response': 'password are not equeal'}, status=400)
            
            if not self.pass_checker.check_password_chars(password):
                return JsonResponse({'response': 'password needs to be stronger with uppercase, lowercase and numbers'}, status=400)
            
            new_user = User(username=username,
                            password=make_password(password))
            new_user.save()

            return JsonResponse({'response': 'user created'}, status=201)
        return JsonResponse({'response': 'missing required data'}, status=400)


class UserLogin(View):
    @method_decorator(require_http_methods(['POST']))
    def post(self, request):

        request_data = json.loads(request.body)
        username = request_data.get('username')

        try:
            current_user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({'response': 'wrong user or password'}, status=404)

        password = request_data.get('password')

        if current_user is not None:
            if check_password(password, current_user.password):
                token = create_jwt(current_user.id)
                refresh_token = create_refresh_token(current_user.id)
                return JsonResponse({'response': {'access_token': token, 'refresh_token': refresh_token}}, status=200)
        return JsonResponse({'response': 'wrong user or password'}, status=401)


class TokenRefresh(View):

    @method_decorator(require_http_methods(['POST']))
    def post(self, request):
        request_data = json.loads(request.body)
        refresh_token = request_data.get('refresh_token')

        try:
            decoded_payload = jwt.decode(
                refresh_token, settings.REFRESH_TOKEN_KEY, algorithms=['HS256'])
            token_type = decoded_payload.get('token_type')
        except jwt.ExpiredSignatureError:
            return JsonResponse({'response': 'token expired'}, status=401)

        except jwt.InvalidTokenError:
            return JsonResponse({'response': 'invalid access token'}, status=401)

        if token_type != 'refresh_token':
            return JsonResponse({'response': 'wrong token type'}, status=401)

        user_id = decoded_payload.get('user_id')
        new_access_token = create_jwt(user_id)

        return JsonResponse({'response': {'new_access_token': new_access_token}}, status=200)


class SwaggerView(View):

    def get(self, request):
        return render(request, 'swagger-ui.html')

