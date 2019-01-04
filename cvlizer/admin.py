from django.contrib import admin
from .models import PersonalInfo, Education, Resume, WorkExperience

# Register your models here.
admin.site.register(PersonalInfo)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Resume)