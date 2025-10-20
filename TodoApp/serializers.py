from rest_framework import serializers
from .models import Profile, Task,ChatMessage

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

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['id', 'createdAt', 'total_tasks', 'pending_tasks', 'completed_tasks']        

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs={
            'profile':{'read_only':True}
        }

    def create(self, validated_data):
        profile =self.context["profile"]
        task = Task.objects.create(profile=profile, **validated_data)
        
        # profile = validated_data.get('profile')
        # if profile:
        #     profile.total_tasks += 1
        #     profile.save()
        return task  
    
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.time_scheduled = validated_data.get('time_scheduled', instance.time_scheduled)
        instance.is_completed = validated_data.get('is_completed', instance.is_completed)
        instance.save()
        return instance

class ChatMessageSerializer(serializers.ModelSerializer):
    reciever_profile = ProfileSerializer(read_only=True)
    sender_profile = ProfileSerializer(read_only=True)
    class Meta:
        model = ChatMessage
        fields = '__all__'
        read_only_fields = ['id', 'timestamp']
         
    
