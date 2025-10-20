from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StoreSerializer,viewStoredFruitSerializer
from .models import FruitStorage
from rest_framework import status


class FruitStorageView(APIView):
    def get(self,request):
        fruits= FruitStorage.objects.all()
        serializer = viewStoredFruitSerializer(fruits, many=True)
        return Response({"Message":serializer.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":serializer.data},status=status.HTTP_201_CREATED)
        return Response({"Error":serializer.errors})
    
class UpdateFruitView(APIView):
    def put(self, request,id):
        obj_id=FruitStorage.objects.get(id=id)
        serializer=StoreSerializer(instance=obj_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":serializer.data},status=status.HTTP_200_OK)
        return Response({"Error":serializer.errors})


    

    
        


