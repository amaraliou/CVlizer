from django.contrib import admin
from .models import PersonalInfo, Education, User, WorkExperience, Project

# Register your models here.
admin.site.register(PersonalInfo)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(User)
admin.site.register(Project)