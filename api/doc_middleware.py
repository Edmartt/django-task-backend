from django.http import JsonResponse
from django.conf import settings

class SwaggerAccess:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
    
    def __call__(self, request):
        if not settings.DEBUG and request.path.startswith('/api/v1/swagger'):
            return JsonResponse({'error': 'docs not available in prod'}, status=404)

        return self.get_response(request)
