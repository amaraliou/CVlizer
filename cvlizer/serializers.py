from rest_framework import serializers
from .models import *

#User serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "pinfo",
            "edus",
            "experiences",
            "projects",
            "skills"
        )
        depth = 1


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
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