from django.contrib import admin
from .models import PersonalInfo, Education, WorkExperience, Project, Skill, User
#from django.conf import settings, delete User

# Register your models here.
admin.site.register(PersonalInfo)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Skill)