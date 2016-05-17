from django.template import loader
from django.http import HttpResponse
from .models import Collection, Movie


def index(request):
    """ Takes in http request, renders the main page. """
    featured_collections = Collection.objects.order_by('creation_date')
    template = loader.get_template('movies/index.html')
    context = {
        'featured_collections': featured_collections,
    }
    return HttpResponse(template.render(context, request))