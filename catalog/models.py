from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey
import uuid
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Ingrese el nombre del género (p. ej. Ciencia Ficción, Acción, Thriller etc.)")

    def __str__(self):
        return self.name

class Director(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    GENRE = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    )

    sexo = models.CharField(max_length=1, choices=GENRE, blank=True, default='o', help_text="(M/F/O)")

    def get_absolute_url(self):
        return reverse('director_detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

class Actor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    GENRE = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    )

    sexo = models.CharField(max_length=1, choices=GENRE, blank=True, default='o', help_text="(M/F/O)")

    def get_absolute_url(self):
        return reverse('actor_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'


class Film(models.Model):
    titulo = models.CharField(max_length=50)
    director = ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    genero = ForeignKey('Genre', on_delete=models.SET_NULL, null=True)
    protagonista = ForeignKey('Actor', on_delete=models.SET_NULL, null=True)
    fecha_salida = models.DateField(null=True, blank=True)
    sinopsis = models.TextField(max_length=1000, null=True, blank=True)
    imagen = models.ImageField(upload_to="imagenes", null=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):

        return reverse('film_detail', args=[str(self.id)])



class FilmInstance(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    pelicula = models.ForeignKey('Film', on_delete=models.SET_NULL, null=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    solicitante = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('p', 'Prestada'),
        ('d', 'Disponible'),
        ('r', 'Reservada'),
    )

    estado = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d')

    class Meta:
        ordering = ['fecha_devolucion']

    def __str__(self):
        return f'{self.id} ({self.pelicula.titulo})'

    def get_absolute_url(self):

        return reverse('filminstance_detail', args=[str(self.id)])

    @property
    def is_overdue(self):
        if self.fecha_devolucion and date.today() > self.fecha_devolucion:
            return True
        return False

    