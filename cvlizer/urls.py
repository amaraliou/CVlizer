from django.urls import path
from .views import *

urlpatterns = [
    path('user/personalinfo', PersonalInfoView.as_view(), name='personal-info'),
    path('user/education', EducationListView.as_view(), name='education'),
    path('user/education/<int:pk>/', EducationSingleView.as_view(), name='education'),
    path('user/workexperience', WorkExperienceView.as_view(), name='work-experience'),
    path('user/project', ProjectsView.as_view(), name='project'),
    path('users', UsersView.as_view(), name='users'),
    path('user/<uuid:uuid_pk>/', UserSingleView.as_view(), name='single-user'),
    path('user/', UserSinglePostView.as_view(), name='single-user-post'),
]
