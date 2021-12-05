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
    list_display = ('last_name', 'first_name', 'sex', 'date_of_birth')

admin.site.register(Actor, ActorAdmin)

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'sex', 'date_of_birth')

admin.site.register(Director, DirectorAdmin)

class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'genre', 'star', 'release_date')
    inlines = [FilmInstanceInline]

admin.site.register(Film, FilmAdmin)


class FilmInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'fecha_devolucion')
    list_display = ('film', 'status', 'borrower', 'fecha_devolucion', 'id')

    fieldsets = (
        (None, {
            'fields': ('film', 'id')
        }),
        ('Disponibilidad', {
            'fields': ('status', 'fecha_devolucion','borrower')
        }),
    )

admin.site.register(FilmInstance, FilmInstanceAdmin)