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
    path('instances/', views.FilmInstanceListView.as_view(), name='filminstance_list'),
    path('contact/', views.index, name='contact'),
    path('film/<int:pk>', views.FilmDetailView.as_view(), name='film_detail'),
    path('instance/<uuid:pk>', views.FilmInstanceDetailView.as_view(), name='filminstance_detail'),
    path('borrowed_films/', views.LoanedFilmsByUserListView.as_view(), name='my_films'),
    path('instance/create/', views.FilmInstanceCreate.as_view(), name='instance_create'),
    path('instance/<uuid:pk>/update/', views.FilmInstanceUpdate.as_view(), name='instance_update'),
    path('instance/<uuid:pk>/delete/', views.FilmInstanceDelete.as_view(), name='instance_delete'),
]