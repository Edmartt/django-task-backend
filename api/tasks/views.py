from django.http import JsonResponse
from django.views import View
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.http import Http404
import json
from .models import Tasks


class Task(View):
    @method_decorator(require_http_methods(['GET']))
    def get(self, request, user_id, task_id=None):

        try:
            user = get_object_or_404(User, id=user_id)
        except Http404:
            return JsonResponse({'response': 'user not found'})
        
        if task_id is not None:

            try:
                task = get_object_or_404(Tasks, id=task_id, user=user)
                task_data = {'title': task.title,
                             'description': task.description}
                return JsonResponse({'task': task_data}, status=200)
            except Http404:
                return JsonResponse({'response': 'task not found'})

        tasks = Tasks.objects.filter(user=user)
        tasks_data = [{'title': task.title,
                       'description': task.description} for task in tasks]

        return JsonResponse({'tasks': tasks_data}, status=200)

    @method_decorator(require_http_methods(['POST']))
    def post(self, request):

        request_data = json.loads(request.body)

        user_id = request_data.get('user_id')

        if user_id is not None:
            user = User.objects.get(id=user_id)
        new_task = Tasks(user=user, title=request_data.get(
            'title'), description=request_data.get('description'))
        new_task.save()

        return JsonResponse({'response': {'id': new_task.id, 'message': 'created'}}, status=201)
