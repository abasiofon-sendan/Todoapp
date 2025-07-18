from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Profile, Task
from .serializers import SignUpSerializers, LogInSerializers, TaskSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(["POST"])
def signup(request):
    serializer = SignUpSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"data":serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"Error":serializer.errors})

@api_view(["POST"])
def login(request):
    serializers = LogInSerializers(data = request.data)
    if serializers.is_valid():
        user = serializers.validated_data['user']
        return Response({"Message":serializers.data}, status=status.HTTP_302_FOUND)
    return Response({"Error":serializers.errors})

@api_view(["POST"])
def add_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"Error":serializer.errors})