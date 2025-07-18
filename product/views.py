from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.parsers import FormParser, MultiPartParser , JSONParser
from rest_framework.decorators import api_view
from .models import Student, School, Students
from .serializers import StudentSerializer, SchoolSerializer


# Create your views here.

TASKS = []
class Hello(APIView):
    def get(self,request):
        return Response({'message' : 'Hello world, '})
    
class Calculus(APIView):
    def post(self, request):
        num1 = request.data.get("num1")
        num2 = request.data.get("num2")

        if not num1 or not num2:
            return Response({"error" : "Please provide num1 and num2"})

        result = int(num1) + int(num2)
        print(result)
        return Response({"sum" : result})
        
class TaskView(APIView):
    def get(self , request):
        return Response({"tasks" : TASKS})
    
    def post(self, request):
        title = request.data.get("title")

        task = {"id" : len(TASKS)+1, "title" : title}
        TASKS.append(task)

        return Response(task, status=status.HTTP_201_CREATED)
    
    def put(self , request):
        task_id = request.data.get("id")
        new_title = request.data.get("title")

        for task in TASKS:
            if task['id'] == task_id:
                task["title"] = new_title  
                return Response ({'message' : "Task Updated", "task": task})

               
        return Response({'error' : "No update was made"}, status = status.HTTP_404_NOT_FOUND) 

    def delete(self, request):
        task_id = request.data.get("id")

        for task in TASKS:
            if task["id"] == task_id:
                TASKS.remove(task)  
                return Response({"message" : "Task deleted"})   

        return Response({"error" : "Task not found"})      

class Email(APIView):

    parser_classes = (FormParser, MultiPartParser, JSONParser)
    def post(self, request):
        name = request.data.get("name")
        email = request.data.get("email")     

        send_mail(
            subject="Abasiofon Sendan  from PY50",
            message=f"Hello {name}, thank you for signing up!",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,)
        print(f"Email sent to {email} with name {name}")
        return Response({"message": "Email sent successfully"}, status=status.HTTP_200_OK)

@api_view(["POST"])   
def create_school(request):
    serializer = SchoolSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"data": serializer.data}, status=201)
  
    return Response({"Error": serializer.errors})

    
@api_view(["POST"])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    
    if serializer.is_valid():
        student = serializer.save()
        return Response({"data": serializer.data}, status=201)
  
    return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def greeting(request):
    return Response({"Message": "Hello world!"})

@api_view(["POST", "GET"])
def student_list_create(request):
    if request.method ==  'GET':
        all_student = Students.objects.all()
        serializer = StudentSerializer(all_student, many=True)
        return Response({"response": serializer.data})
    elif request.method == 'POST':
        serializer = StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data":serializer.data},status=201)
        return Response({"Error":serializer.errors})

    
