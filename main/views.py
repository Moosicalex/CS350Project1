# CS350Project1/main/views.py

from django.shortcuts import render
from django.views.generic import TemplateView

class PlayTemplateView(TemplateView):
    template_name = 'play.html'
