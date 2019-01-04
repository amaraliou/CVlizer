from django.shortcuts import render
from rest_framework import generics
from .models import PersonalInfo, Education, Resume
from .serializers import PISerializer, EducationSerializer, ResumeSerializer

# Create your views here.
class PersonalInfoView(generics.ListAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PISerializer

class EducationView(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class ResumeView(generics.ListAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer