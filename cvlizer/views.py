from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
import uuid

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
        toDelete = Education.objects.filter(pk = pk)
        toDelete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#User views
class UsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserSingleView(APIView):

    def get(self, request, uuid_pk, format = None):
        user = User.objects.filter(pk = uuid_pk)
        serializer = UserSerializer(user, many = True)
        return Response(serializer.data)
    
    def delete(self, request, uuid_pk, format = None):
        toDelete = User.objects.filter(pk = uuid_pk)
        toDelete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class UserSinglePostView(APIView):

    def post(self, request, format = None):
        dt = request.data
        dt['id'] = uuid.uuid4()
        serializer = UserSerializer(data = dt)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)