
from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):

    projects = Project.objects.all() # This will grab all the database objects from model of an app
    return render(request, 'portfolio/home.html', {'projects': projects}) # send database objects to targeted page.
 