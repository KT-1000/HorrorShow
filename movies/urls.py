from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search', views.search, name='search'),
    url(r'^movies', views.movies, name='movies'),
    url(r'^collections', views.collections, name='collections'),
    url(r'^create_collection', views.create_collection, name='create_collection'),
]
