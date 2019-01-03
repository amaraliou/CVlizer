from django.shortcuts import render
from rest_framework import generics
from .models import PersonalInfo
from .serializers import PISerializer

# Create your views here.
class PersonalInfoView(generics.ListAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PISerializer