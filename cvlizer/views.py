from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PersonalInfo, Education, WorkExperience, Project, Skill, User
from .serializers import *
#from django.conf import settings, delete User
import uuid

#Personal Info views
class PersonalInfoView(APIView):

    def get(self, request, username, format = None):
        pinfo = PersonalInfo.objects.all()
        serializer = PISerializer(pinfo, many = True)
        return Response(serializer.data[0], status = status.HTTP_200_OK)
    
    def delete(self, request, username, format = None):
        toDelete = PersonalInfo.objects.all()
        toDelete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, username, format = None):
        pinfo = PersonalInfo.objects.all()
        s = PISerializer(pinfo, many = True)
        if not s.data:
            dt = request.data
            dt['User'] = username
            serializer = PISerializer(data = dt)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Personal Info is already filled, use PUT", status = status.HTTP_401_UNAUTHORIZED)
    
    def put(self, request, username, format = None):
        pinfo = PersonalInfo.objects.all()[:1].get()
        dt = request.data
        serializer = PISerializer(instance = pinfo, data = dt)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


#Project views
class ProjectsListView(APIView):
    
    def get(self, request, username, format = None):
        projects = Project.objects.all()
        serializer = ProjectsSerializer(projects, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request, username, format = None):
        dt = request.data
        dt['User'] = username
        serializer = ProjectsSerializer(data = dt)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectSingleView(APIView):

    def get(self, request, username, pk, format = None):
        project = Project.objects.filter(pk = pk)
        serializer = ProjectsSerializer(project, many = True)
        return Response(serializer.data)

    def delete(self, request, username, pk, format = None):
        toDelete = Project.objects.filter(pk = pk)
        toDelete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, username, pk, format = None):
        toUpdate = Project.objects.filter(pk = pk).first()
        dt = request.data
        dt['User'] = username
        serializer = ProjectsSerializer(instance = toUpdate, data = dt)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


#Education views
class EducationListView(APIView):

    def get(self, request, username, format = None):
        edus = Education.objects.all()
        serializer = EducationSerializer(edus, many = True)
        return Response(serializer.data)

    def post(self, request, username, format = None):
        dt = request.data
        dt['User'] = username
        serializer = EducationSerializer(data = dt)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EducationSingleView(APIView):

    def get(self, request, username, pk, format = None):
        edu = Education.objects.filter(pk = pk)
        serializer = EducationSerializer(edu, many = True)
        return Response(serializer.data)

    def delete(self, request, username, pk, format = None):
        toDelete = Education.objects.filter(pk = pk)
        toDelete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, username, pk, format = None):
        toUpdate = Education.objects.filter(pk = pk).first()
        dt = request.data
        dt['User'] = username
        serializer = EducationSerializer(instance = toUpdate, data = dt, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


#Skill views
class SkillsListView(APIView):

    def get(self, request, username, format = None):
        skillsList = Skill.objects.all()
        serializer = SkillsSerializer(skillsList, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request, username, format = None):
        dt = request.data
        dt['User'] = username
        serializer = SkillsSerializer(data = dt)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SkillSingleView(APIView):

    def get(self, request, username, pk, format = None):
        skillType = Skill.objects.filter(pk = pk)
        serializer = SkillsSerializer(skillType, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def delete(self, request, username, pk, format = None):
        toDelete = Skill.objects.filter(pk = pk)
        toDelete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, username, pk, format = None):
        toUpdate = Skill.objects.filter(pk = pk).first()
        dt = request.data
        dt['User'] = username
        serializer = SkillsSerializer(instance = toUpdate, data = dt, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#User views
class UsersView(APIView):
    
    def get(self, request, format = None):
        users = User.objects.all()
        serializer = UserListSerializer(users, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)


class UserSingleView(APIView):

    def get(self, request, username, format = None):
        user = User.objects.filter(username = username)
        serializer = UserSerializer(user, many = True)
        return Response(serializer.data)
    
    def delete(self, request, username, format = None):
        toDelete = User.objects.filter(username = username)
        toDelete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, username, format = None):
        dt = request.data
        dt['username'] = username
        serializer = UserSerializer(data = dt)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, username, format = None):
        toUpdate = User.objects.filter(username = username).first()
        dt = request.data
        serializer = UserSerializer(instance = toUpdate, data = dt)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)