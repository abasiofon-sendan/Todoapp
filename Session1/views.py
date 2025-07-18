from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

counter = 0

class Home(APIView):
    def get(self,request):
        return Response({'Data': 'welcome Back !!!'})
    
    def post(self, request):
        global counter
        counter += 1
        name = request.data.get('name')
        age = request.data.get('age')

        if not name or not age:

            return Response({"error": "Name and age are required"},status=400)
        else:
            responses = (f"Hello {name}, you are {age} years old")
            print(name)


        return Response({
            "message" : responses,
            "post" : counter
           
        })
        
    
