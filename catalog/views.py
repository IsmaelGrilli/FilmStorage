from django.http.response import Http404
from django.shortcuts import render, redirect
from catalog.models import Film, Director, FilmInstance
from django.views import generic
from django.views.generic import ListView
#from catalog.forms import AuthorForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
    
    num_films = Film.objects.all().count()
    num_instances = FilmInstance.objects.all().count()

    num_instances_available = FilmInstance.objects.filter(status='d').count()

    context = {
        'num_films': num_films,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
    }

    return render(request, 'index.html', context=context)

def film_list(request):
    peliculas = Film.objects.all()
    return render(request, 'film_list.html', context={'peliculas': peliculas})

class FilmListView(generic.ListView):
    model = Film

class FilmDetailView(generic.DetailView):
    model = Film

def film_detail_view(request, primary_key):
    try:
        film = Film.objects.get(pk=primary_key)
    except Film.DoesNotExist:
        raise Http404('La película no existe')

    return render(request, 'catalog/film_detail.html', context={'film': film})

def contact(request):
    datos = {'author': 'Ismael Grilli'}

    return render(request, 'contact.html',
        context=datos)

class LoanedFilmsByUserListView(LoginRequiredMixin, generic.ListView):
    model = FilmInstance
    template_name = "catalog/borrowed_films.html"

    def get_queryset(self):
        return FilmInstance.objects.filter(borrower=self.request.user).filter(status='p').order_by('fecha_devolucion')