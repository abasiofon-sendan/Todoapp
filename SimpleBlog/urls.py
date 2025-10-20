from django.urls import path
from .views import PostView, UpdateDeletePostView,DisplayPosts

urlpatterns =[
    path('posts/', PostView.as_view(), name='posts'),
    path('update/posts/<int:pk>/', UpdateDeletePostView.as_view(), name='update_delete_post'),
    path('displayposts/', DisplayPosts.as_view(), name='display_posts')
]