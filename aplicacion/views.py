from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, "aplicacion/index.html")

def cursos(request):
    contexto = {'Curso': Curso.objects.all()}
    return render(request, "aplicacion/cursos.html", contexto)

def profesores(request):
    return render(request, "aplicacion/cursos.html")

def estudiantes(request):
    return render(request, "aplicacion/cursos.html")

def entregables(request):
    return render(request, "aplicacion/cursos.html")