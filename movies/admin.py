from django.contrib import admin

from .models import Collection, Movie


class CollectionAdmin(admin.ModelAdmin):
    search_fields = ['title']


class MovieAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Collection, CollectionAdmin)
admin.site.register(Movie, MovieAdmin)
