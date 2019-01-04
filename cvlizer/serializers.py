from rest_framework import serializers
from .models import PersonalInfo, Education, User, WorkExperience, Project

class PISerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = (
            "firstName",
            "lastName",
            "email",
            "phone",
            "location",
            "link",
            "User"
        )


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

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "name",
            "pinfo",
            "edus",
            "experiences",
            "projects"
        )
        depth = 1