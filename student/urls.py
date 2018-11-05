from django.urls import path
from student import views as student_views

app_name = 'student'

urlpatterns = [
    path('', student_views.dashboard, name='dashboard'),
]
