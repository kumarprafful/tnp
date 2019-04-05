from django.urls import path
from faculty import views as faculty_views

app_name = 'faculty'

urlpatterns = [
    path('', faculty_views.dashboard, name='dashboard'),
    path('filter', faculty_views.filter, name='filter'),
    path('student-detail/<int:enr>', faculty_views.studentDetail, name='student-detail'),
]
