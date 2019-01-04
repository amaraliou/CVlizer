from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PersonalInfo, Education, User, WorkExperience, Project
from .serializers import PISerializer, EducationSerializer, UserSerializer, WorkExperienceSerializer, ProjectsSerializer

#Personal Info views
class PersonalInfoView(generics.ListAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PISerializer

#Work Experience views
class WorkExperienceView(generics.ListAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

#Project views
class ProjectsView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer

#Education views
class EducationListView(APIView):

    def get(self, request, format = None):
        edus = Education.objects.all()
        serializer = EducationSerializer(edus, many = True)
        return Response(serializer.data)


class EducationSingleView(APIView):

    def get(self, request, pk, format = None):
        edu = Education.objects.filter(pk = pk)
        serializer = EducationSerializer(edu, many = True)
        return Response(serializer.data)

    def post(self, request, pk, format = None):
        dt = request.data
        dt['id'] = pk
        serializer = EducationSerializer(data = dt)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        edu = Education.objects.filter(pk = pk)
        edu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#User views
class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
