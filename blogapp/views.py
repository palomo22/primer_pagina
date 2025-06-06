from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, LibroForm

def index(request):
    return render(request, 'index.html')

def nuevo_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AutorForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Nuevo Autor'})

def nueva_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Nueva Categoría'})

def nuevo_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LibroForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Nuevo Libro'})

#
from .models import Libro
from .forms import BuscarLibroForm
#

def buscar_libro(request):
    resultados = []
    if request.method == 'POST':
        form = BuscarLibroForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultados = Libro.objects.filter(titulo__icontains=titulo)
    else:
        form = BuscarLibroForm()
    return render(request, 'buscar.html', {'form': form, 'resultados': resultados})
