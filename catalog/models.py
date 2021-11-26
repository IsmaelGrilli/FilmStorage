from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey
import uuid
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Ingrese el nombre del género (p. ej. Ciencia Ficción, Acción, Thriller etc.)")

    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)

    GENRE = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    )

    sex = models.CharField(max_length=1, choices=GENRE, blank=True, default='o', help_text="(M/F/O)")

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Actor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)

    GENRE = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    )

    sex = models.CharField(max_length=1, choices=GENRE, blank=True, default='o', help_text="(M/F/O)")

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Film(models.Model):
    title = models.CharField(max_length=50)
    director = ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    genre = ForeignKey('Genre', on_delete=models.SET_NULL, null=True)
    star = ForeignKey('Actor', on_delete=models.SET_NULL, null=True)
    release_date = models.DateField(null=True, blank=True)
    sinopsis = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return '%s, Dir: %s, Actor: %s' % (self.title, self.director, self.star)



class FilmInstance(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    film = models.ForeignKey('Film', on_delete=models.SET_NULL, null=True)
    fecha_devolucion = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('p', 'Prestada'),
        ('d', 'Disponible'),
        ('r', 'Reservada'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d')

    def __str__(self):
        return '%s [%s]' % (self.id, self.film.title)