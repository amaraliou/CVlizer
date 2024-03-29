from rest_framework import serializers
from .models import PersonalInfo, Education, WorkExperience, Project, Skill
from django.contrib.auth import get_user_model
from django.conf import settings

#User serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
            "alias",
            "date_joined",
            "is_staff",
        )
        depth = 1

'''
Example in forms.py:

from django.contrib.auth import UserCreationForm #remove this
from django.contrib.auth.models import User 

class UserSignUpForm(UserCreationForm):
    class Meta:
        fields = ('username', 'password1', 'password2',
                  'email, 'favorite_color',)
        model = User #change this

Post Edit:

from django.contrib.auth get_user_model #add this
from django.contrib.auth import UserCreationForm 

class UserSignUpForm(UserCreationForm):
    class Meta:
        fields = ('username', 'password1', 'password2',
                  'email, 'favorite_color',)
        model = get_user_model() #changed
'''

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "alias",
            "is_staff",
        )


#Personal Info serializer
class PISerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'


#Education serializer
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = (
            "schoolName",
            "schoolLocation",
            "degree",
            "major",
            "gpa",
            "startDate",
            "endDate",
            "relevantCourses",
            "User"
        )


#Work Experience serializer
class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = (
            "companyName",
            "jobTitle",
            "companyLocation",
            "startDate",
            "endDate",
            "jobResp",
            "User"
        )


#Projects serializer
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "projectName",
            "projectDesc",
            "link",
            "tools",
            "User"
        )  


#Skills serializer
class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = (
            "skillType",
            "skillList",
            "User"
        )