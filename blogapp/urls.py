from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('autor/nuevo/', views.nuevo_autor, name='nuevo_autor'),
    path('categoria/nueva/', views.nueva_categoria, name='nueva_categoria'),
    path('libro/nuevo/', views.nuevo_libro, name='nuevo_libro'),
    path('buscar/', views.buscar_libro, name='buscar_libro'),
]
