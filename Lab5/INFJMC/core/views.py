from distutils import core
from django import views
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def home(request):
    return render(request, 'core/index.html')

def carreras(request):
    return render(request, 'core/carreras.html')

def docentes(request):
    return render(request, 'core/docentes.html')