from django.http import JsonResponse
from django.conf import settings
import jwt

class JWTMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        
        token = request.headers.get('Authorization', '').split(' ')[-1]
        
        base_not_protected_route = '/api/v1/users/'
        not_protected_routes = [base_not_protected_route+'login', base_not_protected_route+'signup']
        
        if request.path in not_protected_routes:
            response = self.get_response(request)
            return response
        
        if not token:
            return JsonResponse({'error': 'token missing'}, status=401)
        
        secret_key = settings.JWT_SECRET_KEY
        
        try:
            decoded_payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            request.user_id = decoded_payload.get('user_id')
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'token expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'invalid token'}, status=401)
        
        response = self.get_response(request)
        return response