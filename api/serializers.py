from rest_framework import serializers
from student.models import StudentProfile, ExtraInfo, MarkSheet, WorkExperience, SchoolEducation, CollegeEducation

class StudentProfileSerialzer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'

class ExtraInfoSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = '__all__'

class MarkSheetSerialzer(serializers.ModelSerializer):
    class Meta:
        model = MarkSheet
        fields = '__all__'

class WorkExperienceSerialzer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class SchoolEducationSerialzer(serializers.ModelSerializer):
    class Meta:
        model = SchoolEducation
        fields = '__all__'

class CollegeEducationSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CollegeEducation
        fields = '__all__'
