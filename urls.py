# automation/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.greenhouse_status, name='greenhouse_status'),
]
