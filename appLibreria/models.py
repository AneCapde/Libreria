from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=25)

    def str(self):
        return self.nombre

class Coleccion(models.Model):
    nombreColeccion = models.CharField(max_length=35)
    primeraPublicacion = models.dateField()
    ESTADOS = (
        (FIN, 'Finalizado'),
        (ENCURSO,'En publicación'),
        (PROX, 'No ha salido aún'),
    )

    estado = models.CharField(choices=ESTADOS)

    def str(self):
        return self.nombre

class Comic(models.Model):
    nombreComic = models.CharField(max_length=35)
    numPaginas = models.IntegerField()



    def str(self):
        return self.nombre

class Tag(models.Model):
    descripcion = models.CharField(max_length=25)

    def str(self):
        return self.nombre