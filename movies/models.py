from __future__ import unicode_literals

from django.db import models


class Movie(models.Model):
    """ Movie record from OMDB API. """
    imdb_id = models.CharField(max_length=15, primary_key=True)
    title = models.CharField(max_length=250)
    year = models.DateField(null=True, blank=True)
    rated = models.CharField(max_length=10, blank=True)
    release_date = models.DateField(null=True, blank=True)
    runtime = models.CharField(max_length=15, blank=True)
    genre = models.CharField(max_length=100, blank=True)
    plot = models.TextField(blank=True)
    language = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    poster_url = models.URLField(blank=True)
    poster_loc = models.FilePathField(blank=True)
    imdb_url = models.URLField()
    omdb_url = models.URLField()


class Collection(models.Model):
    """ User-generated groups of movies. """
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    max_size = models.SmallIntegerField(default=25)
    creation_date = models.DateField(null=True, blank=True)
    movies = models.ManyToManyField(Movie)
