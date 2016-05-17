from bs4 import BeautifulSoup
from urllib2 import urlopen
from urllib import urlretrieve
import json
import datetime


def get_movie_ids(out_file):
    """ Get movie information from IMDb to seed horrorshow database.
        Takes out_file, the location of a text file to which imdb_ids will be written.
        Create list of IMDb URLs representing the results for horror genre search
        on IMDb.
        For each URL in the list, open that URL
        Make it into soup
        From each link containing the search result's imdb_id, get the imdb_id
        and write it to the movies.txt file.
        Return list of IMDb IDs.
    """
    # list of imdb id numbers to pass to use in
    imdb_ids = []

    # Get html from URL, format 'http://www.imdb.com/search/title?genres=horror&sort=moviemeter,asc&start=51&title_type=feature'
    html = urlopen("http://www.imdb.com/search/title?genres=horror&sort=moviemeter,asc&title_type=feature")
    soup = BeautifulSoup(html, 'html.parser')

    with open(out_file, 'w') as cur_file:
        for link in soup.find_all('a', href=True):
            # get only links containing imdb id of result movies
            if '/title/tt' in link['href'] and 'vote' not in link['href']:
                # only need movie id
                imdb_id = (link['href'].split('/'))[2]
                # append imdb id number to imdb_ids list, which will be returned
                imdb_ids.append(imdb_id)

        # only want one of each id, so make our array a set
        imdb_ids = set(imdb_ids)
        # write imdb id to file so we can read the file as an alternative to scraping IMDb directly in the future.
        for imdb_id in imdb_ids:
            cur_file.write(imdb_id + '\n')


def get_movie_info(in_file, out_file):
    """ For each imdb_id in the imdb_ids list, query OMDb to get JSON object containing
        information about that movie and write to out_file.
    """
    # list of model json objects
    movies = []
    # open up the ouput file to hold movie data
    with open(out_file, 'w') as movies_file:
        with open(in_file, 'r') as ids_file:
            for imdb_id in ids_file:
                # create URI which will return JSON
                # http://www.omdbapi.com/?i=tt1974419&plot=short&r=json
                omdb_url = "http://www.omdbapi.com/?i=" + imdb_id
                imdb_url = "http://www.imdb.com/title/" + imdb_id.strip()
                response = urlopen(omdb_url)
                data = json.loads(response.read())
                imdb_id = data['imdbID']
                title = data['Title']
                year = data['Year']
                rated = data["Rated"]
                release_date = data['Released']
                release_date = datetime.datetime.strptime(release_date, '%d %b %Y')
                runtime = data['Runtime']
                genre = data['Genre']
                plot = data['Plot']
                language = data['Language']
                country = data['Country']
                poster_url = data['Poster']
                # get local copy of image at poster_url
                # get name of image
                img_name = (poster_url.split('/'))[-1]
                poster_loc = "../static/movie_posters/" + img_name
                # save the image locally
                try:
                    urlretrieve(poster_url, poster_loc)
                except IOError as err:
                    print poster_url + " is not an available image."
                    print err
                    continue

                # Data needs to be in this format
                # [
                #   {
                #     "model": "myapp.person",
                #     "pk": 1,
                #     "fields": {
                #       "first_name": "John",
                #       "last_name": "Lennon"
                #     }
                #   },
                #   {
                #     "model": "myapp.person",
                #     "pk": 2,
                #     "fields": {
                #       "first_name": "Paul",
                #       "last_name": "McCartney"
                #     }
                #   }
                # ]
                # create a new movie model to save to db
                movie = {"model": "movies.movie", "pk": imdb_id, "fields": {}}
                movie["fields"]["title"] = title
                movie["fields"]["year"] = year
                movie["fields"]["rated"] = rated
                movie["fields"]["release_date"] = release_date
                movie["fields"]["runtime"] = runtime
                movie["fields"]["genre"] = genre
                movie["fields"]["plot"] = plot
                movie["fields"]["language"] = language
                movie["fields"]["country"] = country
                movie["fields"]["poster_url"] = poster_url
                movie["fields"]["poster_loc"] = poster_loc
                movie["fields"]["imdb_url"] = imdb_url
                movie["fields"]["omdb_url"] = omdb_url

                print movie

                movies.append(movie)

                # actually save new movie record in db
                # movies.save()
