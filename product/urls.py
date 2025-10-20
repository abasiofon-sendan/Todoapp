from django.urls import path
from .views import Hello, Calculus, TaskView, Email, create_school, create_student, greeting, student_list_create, StudentListCreateView, StudentCreateView,DeleteUpdate

urlpatterns = [
    
    path('greeting/', Hello.as_view(), name='hello'),
    path('calculate/',Calculus.as_view(), name="calculus" ),
    path('taskView/',TaskView.as_view(), name='taskManager'),
    path('email/', Email.as_view(), name='email'),
    path('create_school',create_school, name= "school" ),
    path('create_student', create_student, name="student"),
    path('greeting', greeting, name= "greeting"),
    path('createstudent', student_list_create, name = "Create_student"),
    path('listall',StudentListCreateView.as_view(), name='all'),
    path('create_student_view', StudentCreateView.as_view(), name='create_student_view'),
    path('update-delete/<int:pk>',DeleteUpdate.as_view(), name='updateDelete')

]