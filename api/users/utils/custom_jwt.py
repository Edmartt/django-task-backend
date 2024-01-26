from datetime import datetime, timedelta
import jwt
from django.conf import settings


def create_jwt(user_id: int):
    payload = {
        'user_id': str(user_id),
        'token_type': 'access_token',
        'exp': datetime.utcnow() + timedelta(minutes=1),
        'iat': datetime.utcnow()
    }

    secret_key = settings.JWT_SECRET_KEY
    token = jwt.encode(payload, secret_key, algorithm='HS256')

    return token


def create_refresh_token(user_id: int):
    refresh_payload = {
        'user_id': user_id,
        'token_type': 'refresh_token',
        'exp': datetime.utcnow() + timedelta(minutes=6),
        'iat': datetime.utcnow()
    }

    secret_key = settings.REFRESH_TOKEN_KEY
    refresh_token = jwt.encode(refresh_payload, secret_key, algorithm='HS256')

    return refresh_token
