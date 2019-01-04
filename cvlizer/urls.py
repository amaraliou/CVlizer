from django.urls import path
from .views import PersonalInfoView, EducationView, ResumeView

urlpatterns = [
    path('personalinfo', PersonalInfoView.as_view(), name='personal-info'),
    path('education', EducationView.as_view(), name='education'),
    path('resume', ResumeView.as_view(), name='resume')
]
