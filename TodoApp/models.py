from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.CharField(max_length=100)  
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100, blank= False)
    createdAt = models.DateTimeField(auto_now_add= True)
    total_tasks= models.IntegerField(default=0)  
    pending_tasks = models.IntegerField(default=0)
    completed_tasks = models.IntegerField(default=0)

class Task(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    created_at =  models.DateTimeField(auto_now_add=True)
    time_scheduled = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tasks')

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')    
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')    
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever')   

    message = models.CharField(max_length=500)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering =['timestamp']
        verbose_name_plural = 'Message'

    def __str__(self):
        return f'Message from {self.sender} to {self.reciever} at {self.timestamp}'
    @property
    def sender_profile(self):
        sender_profile = Profile.objects.get(user=self.sender)
        return sender_profile
    
    @property
    def reciever_profile(self):
        reciever_profile = Profile.objects.get(user=self.reciever)
        return reciever_profile
