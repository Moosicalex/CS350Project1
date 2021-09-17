# CS350Project1/end/urls.py

from django.urls import path
from .views import EndTemplateView

urlpatterns = [
    path('', EndTemplateView.as_view(), name='end-template-view'),
]
