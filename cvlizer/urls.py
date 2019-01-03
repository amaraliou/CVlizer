from django.urls import path
from .views import PersonalInfoView

urlpatterns = [
    path('personalinfo', PersonalInfoView.as_view(), name='personal-info')
]
