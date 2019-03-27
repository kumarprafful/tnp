from django.urls import path, include
from api.viewset import *

urlpatterns =[
    path('register/student', StudentRegistrationAPI.as_view(), name="student_register"),
    path('register/faculty', FacultyRegistrationAPI.as_view(), name="faculty_register"),
    path('login', LoginAPI.as_view(), name="login"),
    path('user', UserAPI.as_view(), name="user"),

    path('student/student-profile', StudentProfileViewset.as_view(), name="student-profile"),
    path('student/extra-info', ExtraInfoViewset.as_view(), name="extra-info"),
    path('student/marksheet', MarkSheetViewset.as_view(), name="marksheet"),
    path('student/work-exp', WorkExperienceViewset.as_view(), name="work-exp"),
    path('student/school-education', SchoolEducationViewset.as_view(), name="school-education"),
    path('student/college-education', CollegeEducationViewset.as_view(), name="college-education"),
]
