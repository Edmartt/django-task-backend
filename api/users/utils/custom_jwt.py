from datetime import datetime, timedelta
import jwt
from django.conf import settings

def create_jwt(user_id: int):
    payload = {
        'user_id': str(user_id),
        'exp': datetime.utcnow() + timedelta(seconds=180),
        'iat': datetime.utcnow()      
    }
    
    secret_key = settings.JWT_SECRET_KEY  
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    
    return token

def create_refresh_token(user_id: int):
    refresh_payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=1),
        'iat': datetime.utcnow()
    }
    
    secret_key = settings.REFRESH_TOKEN_KEY
    refresh_token = jwt.encode(refresh_payload, secret_key, algorithm='HS256')
    
    return refresh_token