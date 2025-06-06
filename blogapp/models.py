from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=60)
    autor  = models.ForeignKey(Autor, on_delete=models.CASCADE)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
   
    def __str__(self):
       return self.titulo   