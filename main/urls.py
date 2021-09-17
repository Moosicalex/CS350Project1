# CS350Project1/main/urls.py

from django.urls import path
from .views import PlayTemplateView

urlpatterns = [
    path('', PlayTemplateView.as_view(), name='main-template-view'),
]
