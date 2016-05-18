from django.template import loader
from django.http import HttpResponse
from .models import Collection, Movie


def index(request):
    """ Takes in http request, renders the main page. """
    movies = Movie.objects.order_by('release_date')
    template = loader.get_template('movies/index.html')
    context = {
        'movies': movies,
    }
    return HttpResponse(template.render(context, request))
