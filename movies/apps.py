from __future__ import unicode_literals

from django.apps import AppConfig
from watson import search as watson


class MoviesConfig(AppConfig):
    name = 'movies'

    def ready(self):
        # make Movie model searchable
        movie = self.get_model("Movie")
        watson.register(movie)
        # make Collection model searchable
        collection = self.get_model("Collection")
        watson.register(collection)
