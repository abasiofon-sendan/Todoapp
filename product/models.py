from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)  
    createdAt = models.DateTimeField(auto_now_add= True,blank=True)  
    updatedAt = models.DateTimeField(auto_now_add=True, blank= True) 


class Course(models.Model):
    title = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length= 100)
    courses = models.ManyToManyField(Course)  

    def __str__(self):
        return self.name 

class School(models.Model):
    school_name = models.CharField(max_length= 100)
    def __str__(self):
        return self.school_name
    
class SchoolStudent(models.Model):
    student_name = models.CharField(max_length=100)
    school_attended = models.ForeignKey(School, on_delete=models.CASCADE, related_name="student")    
    
    def __str__(self):
        return self.student_name
    
class Students(models.Model):
    name = models.CharField(max_length= 100)
        
    
