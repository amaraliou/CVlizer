from rest_framework import serializers
from .models import PersonalInfo, Education, Resume

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


class ResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume
        fields = (
            "name",
        )