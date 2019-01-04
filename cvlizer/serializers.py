from rest_framework import serializers
from .models import PersonalInfo, Education, Resume, WorkExperience, Project

class PISerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = (
            "firstName",
            "lastName",
            "email",
            "phone",
            "location",
            "link"
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
            "endDate"
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
            "jobResp"
        )


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "projectName",
            "projectDesc",
            "link",
            "tools"
        )

class ResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume
        fields = (
            "name",
            "pinfo",
            "edus",
            "experiences",
            "projects"
        )
        depth = 1