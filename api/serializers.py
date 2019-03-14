from rest_framework import serializers
from student.models import StudentProfile, ExtraInfo, MarkSheet, WorkExperience, SchoolEducation, CollegeEducation

class StudentProfileSerialzer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'
