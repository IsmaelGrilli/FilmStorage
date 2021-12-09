from django.contrib import admin
from django.db import models

# Register your models here.

from .models import Actor, Director, Genre, Film, FilmInstance

#admin.site.register(Actor)
#admin.site.register(Director)
admin.site.register(Genre)
#admin.site.register(Film)
#admin.site.register(FilmInstance)

class FilmInstanceInline(admin.TabularInline):
    model = FilmInstance

class ActorAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'sexo', 'fecha_nacimiento')

admin.site.register(Actor, ActorAdmin)

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'sexo', 'fecha_nacimiento')

admin.site.register(Director, DirectorAdmin)

class FilmAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'director', 'genero', 'protagonista', 'fecha_salida')
    inlines = [FilmInstanceInline]

admin.site.register(Film, FilmAdmin)


class FilmInstanceAdmin(admin.ModelAdmin):
    list_filter = ('estado', 'fecha_devolucion')
    list_display = ('pelicula', 'estado', 'solicitante', 'fecha_devolucion', 'id')

    fieldsets = (
        (None, {
            'fields': ('pelicula', 'id')
        }),
        ('Disponibilidad', {
            'fields': ('estado', 'fecha_devolucion','solicitante')
        }),
    )

admin.site.register(FilmInstance, FilmInstanceAdmin)