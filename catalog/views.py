from django.db import models
from django.http.response import Http404
from django.shortcuts import render, redirect
from catalog.models import Film, Director, FilmInstance
from django.views import generic
from django.views.generic import ListView
#from catalog.forms import AuthorForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

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

class FilmListView(generic.ListView):
    model = Film

class FilmInstanceListView(generic.ListView):
    model = FilmInstance

class FilmDetailView(generic.DetailView):
    model = Film

class FilmInstanceDetailView(generic.DetailView):
    model = FilmInstance

class FilmInstanceCreate(CreateView):
    model = FilmInstance
    fields = '__all__'
    template_name = "catalog/filminstance_create.html"

class FilmInstanceUpdate(UpdateView):
    model = FilmInstance
    fields = '__all__'
    template_name = "catalog/filminstance_update.html"

class FilmInstanceDelete(DeleteView):
    model = FilmInstance
    success_url = reverse_lazy('instances')

def contact(request):
    datos = {'author': 'Ismael Grilli'}

    return render(request, 'contact.html',
        context=datos)

class LoanedFilmsByUserListView(LoginRequiredMixin, generic.ListView):
    model = FilmInstance
    template_name = "catalog/borrowed_films.html"

    def get_queryset(self):
        return FilmInstance.objects.filter(solicitante=self.request.user).filter(estado='p').order_by('fecha_devolucion')


     