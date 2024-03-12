from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('cursos/', home, name="cursos"),
    path('profesores/', home, name="profesores"),
    path('estudiantes/', home, name="estudiantes"),
    path('entregables/', home, name="entregables"),
]