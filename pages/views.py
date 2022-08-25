from pipes import Template
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class DashboardPageView(TemplateView):
    template_name = 'dashboard.html'

class MapPageView(TemplateView):
    template_name = 'map.html'
