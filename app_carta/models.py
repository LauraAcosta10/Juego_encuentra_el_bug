from django.db import models

# Create your models here.

class Carta_programador(models.Model):
    nombre = models.CharField('Nombre del programador', max_length=30)

    def __str__(self):
        return self.nombre

class Carta_modulo(models.Model):
    nombre = models.CharField('Nombre del modulo', max_length=30)

    def __str__(self):
        return self.nombre

class Carta_bug(models.Model):
    nombre = models.CharField('Nombre del bug', max_length=30)

    def __str__(self):
        return self.nombre