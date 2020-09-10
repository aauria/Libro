from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre=models.CharField(max_length=100)
    fecha=models.DateField()


class Editorial(models.Model):
    nombre = models.CharField(max_length=100)



class Libro(models.Model):
    isbn=models.CharField(max_length=20)
    titulo=models.CharField(max_length=50)
    autor=models.ForeignKey(Autor,on_delete=models.CASCADE)
    editorial=models.ForeignKey(Editorial,on_delete=models.CASCADE)
    precio=models.IntegerField()
