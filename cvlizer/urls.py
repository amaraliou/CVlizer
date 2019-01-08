from django.urls import path
from .views import *

urlpatterns = [
    path('user/<uuid:uuid_pk>/personalinfo', PersonalInfoView.as_view(), name='personal-info'),
    path('user/<uuid:uuid_pk>/education', EducationListView.as_view(), name='education'),
    path('user/<uuid:uuid_pk>/education/<int:pk>/', EducationSingleView.as_view(), name='education'),
    path('user/<uuid:uuid_pk>/skills', SkillsListView.as_view(), name = 'skills'),
    path('user/<uuid:uuid_pk>/projects', ProjectsListView.as_view(), name='project'),
    path('users', UsersView.as_view(), name='users'),
    path('user/<uuid:uuid_pk>/', UserSingleView.as_view(), name='single-user'),
]
