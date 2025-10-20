from django.urls import path
from .views import signup, login,features,MyInbox

urlpatterns=[
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path("features/<int:user_id>",features, name = 'features'),
    # path("get_task",get_task, name='task_lisk'),
    # path("update_task/<int:pk>", update_task, name='update_task'),
    # path("message", message, name='message')
    path("message/<int:user_id>", MyInbox.as_view(), name='message'),
]