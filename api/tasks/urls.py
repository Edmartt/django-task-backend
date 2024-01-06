from django.urls import path
from .views import Task

urlpatterns = [
    path('users/<int:user_id>/tasks/<int:task_id>', Task.as_view(), name='Task'),
    path('users/<int:user_id>/tasks', Task.as_view(), name='Task'),
    path('users/<int:user_id>/tasks', Task.as_view(), name='Task')
]
