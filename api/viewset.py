from rest_framework.views import APIView
from rest_framework.response import Response
from student.models import StudentProfile, ExtraInfo, MarkSheet, WorkExperience, SchoolEducation, CollegeEducation
from api.serializers import StudentProfileSerialzer

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
