from django.shortcuts import render
from django.views.generic import TemplateView
from django import forms


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

# Create your views here.
