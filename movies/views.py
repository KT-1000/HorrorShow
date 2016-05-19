from django.template import loader
from django.http import HttpResponse
from .models import Collection, Movie
from utils import generic_search
from django.shortcuts import render_to_response, redirect


def index(request):
    """ Takes in http request, renders the main page. """
    movies = Movie.objects.order_by('release_date')
    template = loader.get_template('movies/index.html')
    context = {
        'movies': movies,
    }
    return HttpResponse(template.render(context, request))


def search(request):
    """ Takes in http request, returns the search_results html
        with the objects found by the search available to that template.
    """
    query = "search-query"
    # model fields to return
    model_map = {Movie: ["title", "year", "plot", "release_date", "poster_loc"], Collection: ["title", "description", "creation_date", "movies"]}

    # list of return results
    returned_objects = []

    for model, fields in model_map.iteritems():
        returned_objects += generic_search(request, model, fields, query)

    return render_to_response("movies/search_results.html",
                              {"results": returned_objects,
                               "search_string": request.GET.get(query, "")
                               }
                              )

# def collection(request):
#     """ Takes in http request, renders the page containing the form to create collections. """
#