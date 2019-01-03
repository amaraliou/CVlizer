from rest_framework import serializers
from .models import PersonalInfo

class PISerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = ("firstName",
                  "lastName",
                  "email",
                  "phone",
                  "location",
                  "link")