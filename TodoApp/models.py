from django.db import models

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