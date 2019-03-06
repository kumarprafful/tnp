from django.contrib import admin
from student.models import StudentProfile, MarkSheet, ExtraInfo, WorkExperience, CollegeEducation, SchoolEducation

# Register your models here.
admin.site.register(StudentProfile,list_display=['name', 'course', 'enrollment_no'], search_fields=('enrollment_no', 'name'))
admin.site.register(MarkSheet)
admin.site.register(ExtraInfo)
admin.site.register(WorkExperience)
admin.site.register(SchoolEducation)
admin.site.register(CollegeEducation)
