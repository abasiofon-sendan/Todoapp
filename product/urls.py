from django.urls import path
from .views import Hello, Calculus, TaskView, Email, create_school, create_student, greeting, student_list_create

urlpatterns = [
    
    path('greeting/', Hello.as_view(), name='hello'),
    path('calculate/',Calculus.as_view(), name="calculus" ),
    path('taskView/',TaskView.as_view(), name='taskManager'),
    path('email/', Email.as_view(), name='email'),
    path('create_school',create_school, name= "school" ),
    path('create_student', create_student, name="student"),
    path('greeting', greeting, name= "greeting"),
    path('createstudent', student_list_create, name = "Create_student")


]