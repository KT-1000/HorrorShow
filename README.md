# HorrorShow
Hackbright Final Project

Initial Setup
======================================================================================================
Create postgreSQL database called horrorshow.

From manage.py, 
  migrate to set up your database tables based on app models.
  
  createsuperuser using the credentials you prefer.
  
  loaddata movies.json to populate the database.
  
  installwatson to enable search feature.
  
  buildwatson to create search indexing.

To create the movis.json, in HorroShow/movies/fixtures/, run: 
  python -i data_import.py
  
In this interactive python prompt, if movie_ids.txt, movie_info.txt and/or movies.json do not exist, 
or contain outdated information, run the appropriate function(s).

For example:
  get_movie_ids("movie_ids.txt")
will get imdb_ids from http://www.imdb.com/search/title?genres=horror&sort=moviemeter,asc&title_type=feature&start=1.

  get_movie_info("movie_ids.txt", "movie_info.txt")
will parse movie_ids.txt for imdb ids and hit the omdb api to get information about the movies.

  get_movie_json("movie_info.txt", "movies.json")
will format this data in json and import into the horrorshow database previously created.

It is important to note that these steps will only populate the Movie table.
To create Collection records, you must runserver and go to the admin panel until the create collection functionality is implemented.
