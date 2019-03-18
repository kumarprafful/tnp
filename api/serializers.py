from django.contrib.auth import authenticate
from account.models import User
from rest_framework import serializers, generics
from student.models import StudentProfile, ExtraInfo, MarkSheet, WorkExperience, SchoolEducation, CollegeEducation
from knox.models import AuthToken


class CreateStudentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['enrollment_no', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['password'], validated_data['enrollment_no'])
        return user

class CreateFacultyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['password'])
        return user

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Credentials wrong")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

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
