from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.user_login, name='user_login'),
    url(r'^logout', views.user_logout, name='user_logout'),
    url(r'^search', views.search, name='search'),
    url(r'^movies', views.movies, name='movies'),
    url(r'^collections', views.collections, name='collections'),
    url(r'^create_collection', views.create_collection, name='create_collection'),
    url(r'^movie/(?P<imdb_id>[\w\-]+)/$', views.movie_detail, name='movie_detail'),
    url(r'^collection/(?P<collection_id>[0-9]+)/$', views.collection_detail, name='collection_detail'),
]
