from typing_extensions import Required
from django.db import models
from django.http.response import Http404
from django.shortcuts import render, redirect
from catalog.models import Film, Director, FilmInstance
from django.views import generic
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

#Vista función de la página principal, devuelve varios valores relacionados con las películas y los ejemplares disponibles
def index(request):
    
    num_films = Film.objects.all().count()
    num_instances = FilmInstance.objects.all().count()

    num_instances_available = FilmInstance.objects.filter(estado='d').count()

    context = {
        'num_films': num_films,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
    }

    return render(request, 'index.html', context=context)

#Vistas clases
#Vista utilizada para mostrar el listado de películas
class FilmListView(generic.ListView):
    model = Film

#Vista utilizada para mostrar el listado de ejemplares
class FilmInstanceListView(LoginRequiredMixin, generic.ListView):
    model = FilmInstance

#Vista utilizada para mostrar el detalle de las películas
class FilmDetailView(generic.DetailView):
    model = Film

#Vista utilizada para mostrar el detalle de los ejemplares
class FilmInstanceDetailView(LoginRequiredMixin, generic.DetailView):
    model = FilmInstance

#Vista que permite crear ejemplares y se relaciona con el formulario de creación
class FilmInstanceCreate(LoginRequiredMixin, CreateView):
    model = FilmInstance
    fields = '__all__'
    template_name = "catalog/filminstance_create.html"

#Vista que permite actualizar ejemplares y se relaciona con el formulario de actualización
class FilmInstanceUpdate(LoginRequiredMixin, UpdateView):
    model = FilmInstance
    fields = '__all__'
    template_name = "catalog/filminstance_update.html"

#Vista que permite eliminar ejemplares
class FilmInstanceDelete(LoginRequiredMixin, DeleteView):
    model = FilmInstance
    success_url = reverse_lazy('filminstance_list')

#Vista que permite obtener los ejemplares que han sido solicitados por el usuario activo
class LoanedFilmsByUserListView(LoginRequiredMixin, generic.ListView):
    model = FilmInstance
    template_name = "catalog/borrowed_films.html"

    def get_queryset(self):
        return FilmInstance.objects.filter(solicitante=self.request.user).filter(estado='p').order_by('fecha_devolucion')


     