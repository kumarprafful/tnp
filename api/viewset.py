from rest_framework.views import APIView
from rest_framework.response import Response
from student.models import StudentProfile, ExtraInfo, MarkSheet, WorkExperience, SchoolEducation, CollegeEducation
from api.serializers import StudentProfileSerialzer, ExtraInfoSerialzer, MarkSheetSerialzer, WorkExperienceSerialzer, SchoolEducationSerialzer, CollegeEducationSerialzer

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
