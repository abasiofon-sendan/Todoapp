from rest_framework import serializers
from .models import FruitStorage

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model=FruitStorage
        fields='__all__'
        read_only_field=['id']

class viewStoredFruitSerializer(serializers.ModelSerializer):
    class Meta:
        model=FruitStorage
        fields=['name','price']
        read_only_field=['id']        
       
# class updateFruitSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=FruitStorage
#         fields=['name','price']

