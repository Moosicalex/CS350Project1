# CS350Project1/start/urls.py

from django.urls import path
from .views import StartTemplateView

urlpatterns = [
    path('', StartTemplateView.as_view(), name='start-template-name'),
]
