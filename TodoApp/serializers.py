from rest_framework import serializers
from .models import Profile, Task

class SignUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class LogInSerializers(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('passowrd')
        
        try:
            user = Profile.objects.get(email = email)
        except Profile.DoesNotExist:
            raise serializers.ValidationError("User not found")
        
        data['user'] = user
        return data

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        task = Task.objects.create(**validated_data)
        profile = validated_data.get('profile')
        # profile = Profile.objects.get(id=profile_id)
        # profile.total_tasks += 1
        # profile.pending_tasks += 1
        if profile:
            profile.total_tasks += 1
            profile.save()
        return task    

