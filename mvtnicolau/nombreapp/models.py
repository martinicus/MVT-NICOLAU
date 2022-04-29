from django.db import models

# Create your models here.


class Mi_familia(models.Model):
    parentaje=models.CharField(max_length=40)
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    edad=models.IntegerField()
    ocupacion=models.CharField(max_length=40)
    email=models.EmailField(max_length = 254)

    