# HorrorShow

HorrorShow is a web application created by Katie Simmons. Horror movie fans can create collections of horror movies via a form, and browse others' collections. Rich information, including trailers and where to stream or purchase movies, is pulled directly from a PostgreSQL database populated from three separate sources (IMDb, OMDb, Guidebox). Since this db is indexed using watson, users can also search for movies and collections.

## <a name="technologiesused"></a>Technologies Used
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [PostGreSQL](https://www.postgresql.org/)
- [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [OMDb API](http://www.omdbapi.com/)
- [Guidebox API](https://api.guidebox.com/)
= [Watson](https://github.com/etianen/django-watson)
- [Bootstrap](http://getbootstrap.com/)

## <a name="features"></a>Features

*Current*

- [X] HorrorShow database contains comprehensive information about movies.
- [X] Full-text search returns movies and collections associated with user-entered term.
- [X] Authenticated users can create collections with title, description and 25 or fewer movies.

*Future*

- [ ] Users can share collections.
- [ ] Movies and collections are suggested based on user ratings.

## <a name="searchfunction"></a>Search Function

## <a name="data"></a>Data

The ETL process was the primary challenge and very core of this project. Since my initial chosen library to obtain movie information relied on a deprecated dependency that prevented it from being used successfully on any of the OSes or Python versions I tried, it was necessary to seek data from diverse sources. Initially, this meant using BeautifulSoup4 to scrape IMDb for horror movie IDs that could be used in other APIs. With IMDB IDs, I could format OMDb and Guidebox URLs to GET JSON. For each model corresponding to a database table, the fields came from IMDb, OMDb and Guidebox. Since Guidebox provided posters, trailers, streaming sources, and other data, I determined that it would be most effective to leverage PostgreSQL's JSON field and store the Guidebox data in its JSON format.

Less than a week prior to the "due date", my laptop died, so I bought a new one, configured it appropriately and tried to recreate my database. This allowed me to really streamline the process and concentrate on scalabilty. Currently, the data import is able to grab information for 17491 titles out of about 19200, spaced out appropriately so as not to overload any single point.
