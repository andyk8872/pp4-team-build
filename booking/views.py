from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "index.html"
