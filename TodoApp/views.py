from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Profile, Task,ChatMessage
from .serializers import SignUpSerializers, LogInSerializers, TaskSerializer, ChatMessageSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.db.models import Subquery, OuterRef, Q
from django.contrib.auth.models import User


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
        return Response({"Message":"login successfull"}, status=status.HTTP_302_FOUND)
    return Response({"Error":serializers.errors})

@api_view(['GET','PUT','POST'])
def features(request,user_id):
    user=Profile.objects.get(id=user_id)
    
    if request.method == "GET":
        list_task = Task.objects.filter(profile = user)
        serializer = TaskSerializer(list_task, many=True)
        return Response({"data":serializer.data},status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = TaskSerializer(data=request.data,context={'profile':user})
        if serializer.is_valid():
            serializer.save()
            return Response({"data": "Task Created"}, status=status.HTTP_201_CREATED)
        return Response({"Error":serializer.errors})
    
    # elif request.method == "PUT":
    #     try:
    #         task = Task.objects.get(pk=id)
    #     except Task.DoesNotExist:
    #         return Response({"Error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    #     serializer = TaskSerializer(instance=task, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    #     return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    

# @api_view(["GET"])
# def get_task(request):


# @api_view(["PUT"])
# def update_task(request, pk):


    
# @api_view(['GET','PUT','POST'])
# def message(request):
#     return Response({"message":"Hello, this is a message from the TodoApp!"}, status=status.HTTP_200_OK)


class MyInbox(generics.ListAPIView):
    serializer_class = ChatMessageSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']

        messages = ChatMessage.objects.filter(
            id__in=Subquery(
                User.objects.filter(
                    Q(sender_reciever=user_id) |
                    Q(reciever_sender=user_id)
                ).distinct().annotate(
                    last_msg=Subquery(
                        ChatMessage.objects.filter(
                            Q(sender=OuterRef('id'),reciever=user_id) |
                            Q(reciever=OuterRef('id'),sender=user_id)
                        ).order_by('-id')[:1].values_list('id',flat=True)
                    )
                    
                ).values_list('last_msg', flat=True).order_by("-id")
            )
        ).order_by("-id")

        return messages
