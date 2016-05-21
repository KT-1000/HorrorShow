from __future__ import unicode_literals

from django.apps import AppConfig
from watson import search as watson


class MoviesConfig(AppConfig):
    name = 'movies'

    def ready(self):
        # make Movie model searchable
        Movie = self.get_model("Movie")
        watson.register(Movie)
        # make Collection model searchable
        Collection = self.get_model("Collection")
        watson.register(Collection)
