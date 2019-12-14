from django.urls import path
from .views import *


app_name = 'Administrator'

urlpatterns = [
    path('', BaseInfoView.as_view(), name='login_logout'),
    path('register/', RegisterView.as_view(), name='register'),
]