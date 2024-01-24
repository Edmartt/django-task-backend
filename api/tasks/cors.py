from django.http import HttpResponse

class CorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        if request.method == 'OPTIONS':
            response = HttpResponse(status=200)
            self.add_cors_headers(response)
            return response
        
        response = self.get_response(request)
        self.add_cors_headers(response)
        return response

    def add_cors_headers(self, response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response
