from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Collection, Movie
from django.shortcuts import get_object_or_404, redirect
from watson import search as watson
from fixtures import data_import as di


def index(request):
    """ Takes in http request, renders the main page. """
    qs_recent_movies = Movie.objects.order_by('-release_date')
    recent_movies = None
    if len(qs_recent_movies):
        recent_movies = qs_recent_movies[:12]

    qs_featured_collection = Collection.objects.order_by('creation_date')
    featured_collection = None
    if len(qs_featured_collection):
        featured_collection = qs_featured_collection[0]

    # get featured collection(s)
    template = loader.get_template('movies/index.html')
    context = {
        'recent_movies': recent_movies,
        'featured_collection': featured_collection,
    }
    return HttpResponse(template.render(context, request))


def search(request):
    """ Takes in http request and a user-entered search string, returns the search_results html
        with the objects found by the search available to that template.
    """
    search_str = request.GET["user_search"]
    search_results = watson.search(search_str)
    template = loader.get_template('movies/search_results.html')
    context = {
        'search_results': search_results,
        'search_str': search_str,
    }

    return HttpResponse(template.render(context, request))


def movies(request):
    """ Takes in http request, renders all movies, ordered by release date, paginated. """
    movies = Movie.objects.order_by('-release_date')
    template = loader.get_template('movies/movies.html')
    context = {
        'movies': movies,
    }
    return HttpResponse(template.render(context, request))


def movie_detail(request, imdb_id):
    """ Takes in request and IMDb ID to provide movie detail view """
    movie = get_object_or_404(Movie, imdb_id=imdb_id)
    template = loader.get_template('movies/movie_detail.html')
    context = {
        'movie': movie,
    }
    return HttpResponse(template.render(context, request))


def collections(request):
    """ Takes in http request, renders all collections, ordered by creation date, paginated. """
    # get all collections ordered with most recent creation date first
    collections = Collection.objects.order_by('-creation_date')
    template = loader.get_template('movies/collections.html')
    context = {
        'collections': collections,
    }
    return HttpResponse(template.render(context, request))


def collection_detail(request, collection_id):
    """ Takes in request and IMDb ID to provide movie detail view """
    # get collection based on the collection id
    collection = get_object_or_404(Collection, id=collection_id)

    template = loader.get_template('movies/collection_detail.html')
    context = {
        'collection': collection,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def create_collection(request):
    """ Takes http request, renders the page containing the form to create collections. """
    pass


def guidebox_import(request):
    """"""
    qs_movies = Movie.objects.all()
    for movie in qs_movies:
        movie.guidebox_data = di.guidebox_import(movie.guidebox_id)
        movie.save()

    return redirect('/HorrorShow')


def omdb_import(request):
    """"""
    di.get_movie_info("movies/fixtures/movie_ids.txt", "movies/fixtures/movie_info.txt")
    di.get_movie_json("movies/fixtures/movie_info.txt", "movies/fixtures/movies.json")

    return redirect('/HorrorShow')
