from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User


class MovieManager(models.Manager):
    """ Provides methods to create movie instances. """
    # to make a movie, call movie = Movie.objects.create_movie(<params>)
    def create_movie(self,
                     imdb_id,
                     guidebox_id,
                     title,
                     year,
                     rated,
                     release_date,
                     runtime,
                     genre,
                     plot,
                     language,
                     country,
                     poster_url,
                     poster_loc,
                     imdb_url,
                     omdb_url,
                     guidebox_data):
        """ Make an instance of the Movie class.
            Takes in imdb_id,
                guidebox_id,
                title,
                year,
                rated,
                release_date,
                runtime,
                genre,
                plot,
                language,
                country,
                poster_url,
                poster_loc,
                imdb_url,
                omdb_url,
                guidebox_data.
            Returns the Movie object created.
        """
        movie = self.create(imdb_id=imdb_id,
                            guidebox_id=guidebox_id,
                            title=title,
                            year=year,
                            rated=rated,
                            release_date=release_date,
                            runtime=runtime,
                            genre=genre,
                            plot=plot,
                            language=language,
                            country=country,
                            poster_url=poster_url,
                            poster_loc=poster_loc,
                            imdb_url=imdb_url,
                            omdb_url=omdb_url,
                            guidebox_data=guidebox_data)

        return movie


class Movie(models.Model):
    """ Movie record from OMDB API. """
    imdb_id = models.CharField(max_length=15, primary_key=True)
    guidebox_id = models.CharField(max_length=15, null=True, blank=True)
    title = models.CharField(max_length=250)
    year = models.DateField(null=True, blank=True)
    rated = models.CharField(max_length=10, blank=True)
    release_date = models.DateField(null=True, blank=True)
    runtime = models.CharField(max_length=15, blank=True)
    genre = models.CharField(max_length=250, blank=True)
    plot = models.TextField(blank=True)
    language = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    poster_url = models.URLField(max_length=500, blank=True)
    poster_name = models.CharField(max_length=100, blank=True)
    imdb_url = models.URLField(max_length=500)
    omdb_url = models.URLField(max_length=500)
    guidebox_data = JSONField(null=True, blank=True)
    has_poster = models.NullBooleanField(null=True, blank=True)

    objects = MovieManager()

    def __str__(self):
        return self.title


class CollectionManager(models.Manager):
    """ Provides methods to manage cretion of collections. """
    # to make a collection, collection = Collection.objects.create_collection(<params>)
    def create_collection(self, title, description, max_size, creation_date, movies, user):
        """ Make an instance of the colleciton class.
            Takes in title, description, max_size, creation_date, movies
            Returns the Collection object created.
        """
        collection = self.create(title=title,
                                 description=description,
                                 max_size=max_size,
                                 creation_date=creation_date,
                                 movies=movies,
                                 user=user)

        return collection


class Collection(models.Model):
    """ User-generated groups of movies. """
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    max_size = models.SmallIntegerField(default=25)
    creation_date = models.DateField(null=True, blank=True)
    movies = models.ManyToManyField(Movie)
    user = models.ForeignKey(User, null=True, blank=True)

    objects = CollectionManager()

    def __str__(self):
        return self.title
