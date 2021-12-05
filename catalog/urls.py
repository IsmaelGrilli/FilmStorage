from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings, urls
from django.conf.urls.static import static
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('film_list/', views.FilmListView.as_view(), name='film_list'),
    path('contact/', views.index, name='contact'),
    path('film/<int:pk>', views.FilmDetailView.as_view(), name='film_detail'),
    path('borrowed_films/', views.LoanedFilmsByUserListView.as_view(), name='my_films'),
]