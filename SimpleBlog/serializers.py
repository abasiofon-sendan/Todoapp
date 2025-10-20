from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['title','content','author','created_at','post_images']
        read_only_fields=['id','created_at','author']