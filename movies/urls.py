from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.user_login, name='login'),
    url(r'^logout', views.user_logout, name='logout'),
    url(r'^search', views.search, name='search'),
    url(r'^movies', views.movies, name='movies'),
    url(r'^collections', views.collections, name='collections'),
    url(r'^create_collection', views.create_collection, name='create_collection'),
    url(r'^movie/(?P<pk>[\w\-]+)/$', views.movie_detail, name='movie'),
    url(r'^collection/(?P<pk>\d+)/$', views.collection_detail, name='collection'),
]
