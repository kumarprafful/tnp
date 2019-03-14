from django.urls import path
from api.viewset import StudentProfileViewset, ExtraInfoViewset, MarkSheetViewset, WorkExperienceViewset, SchoolEducationViewset, CollegeEducationViewset

urlpatterns =[
    path('student/student-profile', StudentProfileViewset.as_view(), name="student-profile"),
    path('student/extra-info', ExtraInfoViewset.as_view(), name="extra-info"),
    path('student/marksheet', MarkSheetViewset.as_view(), name="marksheet"),
    path('student/work-exp', WorkExperienceViewset.as_view(), name="work-exp"),
    path('student/school-education', SchoolEducationViewset.as_view(), name="school-education"),
    path('student/college-education', CollegeEducationViewset.as_view(), name="college-education"),


]
