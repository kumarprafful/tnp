from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from knox.models import AuthToken

from student.models import StudentProfile, ExtraInfo, MarkSheet, WorkExperience, SchoolEducation, CollegeEducation
from api.serializers import *

class StudentRegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateStudentUserSerializer
    def post(self, request, *args, **kwargs):
        print("YESS")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })

class FacultyRegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateFacultyUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })

class StudentProfileViewset(APIView):
    def get(self, request, format=None):
        queryset = StudentProfile.objects.all()
        serializer = StudentProfileSerialzer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentProfileSerialzer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ExtraInfoViewset(APIView):
    def get(self, request, format=None):
        queryset = ExtraInfo.objects.all()
        serializer = ExtraInfoSerialzer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExtraInfoSerialzer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MarkSheetViewset(APIView):
    def get(self, request, format=None):
        queryset = MarkSheet.objects.all()
        serializer = MarkSheetSerialzer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MarkSheetSerialzer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class WorkExperienceViewset(APIView):
    def get(self, request, format=None):
        queryset = WorkExperience.objects.all()
        serializer = WorkExperienceSerialzer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WorkExperienceSerialzer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SchoolEducationViewset(APIView):
    def get(self, request, format=None):
        queryset = SchoolEducation.objects.all()
        serializer = SchoolEducationSerialzer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SchoolEducationSerialzer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CollegeEducationViewset(APIView):
    def get(self, request, format=None):
        queryset = CollegeEducation.objects.all()
        serializer = CollegeEducationSerialzer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CollegeEducationSerialzer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
