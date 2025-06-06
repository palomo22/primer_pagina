# Entrega 3 Python Crear una web tipo Blog basica utilizando Django y el patron MVT (modelo vista plantilla)
## Estructura

- Proyecto Django: `primer_pagina`
- App principal: `webapp`
- Base de datos: SQLite (por defecto en Django)
- Formularios para insertar datos en:
  - Autor
  - Categoría
  - Libro
- Búsqueda de libros por título
- Herencia de templates con `base.html`

## Requisitos

- Python 3.x
- Django 4+

## Cómo ejecutar el proyecto:

- Clonar este repositorio: 

# Funcionalidades

- `/` — Página de inicio
- `/autor/nuevo/` — Formulario para agregar un autor
- `/categoria/nueva/` — Formulario para agregar una categoría
- `/libro/nuevo/` — Formulario para agregar un libro
- `/buscar/` — Formulario de búsqueda de libros por título