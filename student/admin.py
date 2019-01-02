from django.contrib import admin
from student.models import StudentProfile, MarkSheet

# Register your models here.
admin.site.register(StudentProfile,list_display=['name', 'course', 'enrollment_no'], search_fields=('enrollment_no', ))
admin.site.register(MarkSheet)
