from rest_framework import serializers
from .models import PersonalInfo, Education, User, WorkExperience, Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "pinfo",
            "edus"
        )
        depth = 1


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
        )

class PISerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'


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
            "User"
        )


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

    
    