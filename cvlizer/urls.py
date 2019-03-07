from django.urls import path
from .views import *

urlpatterns = [
    #Users urls
    path('users', UsersView.as_view(), name='users'),
    path('user/<str:username>/', UserSingleView.as_view(), name='single-user'),
    #Personal Info url
    path('user/<str:username>/personalinfo', PersonalInfoView.as_view(), name='personal-info'),
    #Education urls
    path('user/<str:username>/education', EducationListView.as_view(), name='education'),
    path('user/<str:username>/education/<int:pk>', EducationSingleView.as_view(), name='single-education'),
    #Skills urls
    path('user/<str:username>/skills', SkillsListView.as_view(), name = 'skills'),
    path('user/<str:username>/skills/<int:pk>', SkillSingleView.as_view(), name = 'single-skill'),
    #Projects urls
    path('user/<str:username>/projects', ProjectsListView.as_view(), name='projects'),
    path('user/<str:username>/projects/<int:pk>', ProjectSingleView.as_view(), name='single-project'),
]
