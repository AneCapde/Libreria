from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    anyoNacimiento = models.IntegerField()

    def str(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('autorDetail', args=[str(self.pk)])

class Tag(models.Model):
    descripcion = models.CharField(max_length=25)

    def str(self):
        return self.descripcion
        
class Coleccion(models.Model):
    nombreColeccion = models.CharField(max_length=35)
    primeraPublicacion = models.DateField()
    autores = models.ManyToManyField(Autor)
    tags = models.ManyToManyField(Tag)

    ESTADOS = (
        ('FIN', 'Finalizado'),
        ('ENCURSO','En publicación'),
        ('PROX', 'Sin publicar'),
    )

    estado = models.CharField(choices=ESTADOS, max_length=40)

    def str(self):
        return self.nombreColeccion
    
    def get_absolute_url(self):
        return reverse('coleccionDetail', args=[str(self.pk)])

class Comic(models.Model):
    nombreComic = models.CharField(max_length=35)
    numPaginas = models.IntegerField()
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE, default=0)

    def str(self):
        return self.nombreComic
    
    def get_absolute_url(self):
        return reverse('comicDetail', args=[str(self.pk)])
