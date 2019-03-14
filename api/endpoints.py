from django.urls import path
from api.viewset import StudentProfileViewset

urlpatterns =[
    path('student/student-profile', StudentProfileViewset.as_view(), name="student-profile"),

]
