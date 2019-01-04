from django.urls import path
from .views import PersonalInfoView, EducationView, ResumeView, WorkExperienceView, ProjectsView

urlpatterns = [
    path('resume/personalinfo', PersonalInfoView.as_view(), name='personal-info'),
    path('resume/education', EducationView.as_view(), name='education'),
    path('resume/workexperience', WorkExperienceView.as_view(), name='work-experience'),
    path('resume/project', ProjectsView.as_view(), name='project'),
    path('resume', ResumeView.as_view(), name='resume')
]
