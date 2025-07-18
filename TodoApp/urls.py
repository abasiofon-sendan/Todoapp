from django.urls import path
from .views import signup, login, add_task, get_task

urlpatterns=[
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path("add_task",add_task, name = 'add_task'),
    path("get_task",get_task, name='task_lisk')
]