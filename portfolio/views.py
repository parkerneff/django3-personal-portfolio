from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Project


def home(request):
    projects = Project.objects.all()
    template = loader.get_template('portfolio/home.html')
    return HttpResponse(template.render({'projects': projects}, request))
