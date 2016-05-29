# HorrorShow
Hackbright Final Project

Initial Setup
======================================================================================================
Create postgreSQL database called horrorshow.

From manage.py, 
  migrate 
  to set up your database tables based on app models.
  
  createsuperuser 
  using the credentials you prefer.
  
  loaddata movies.json 
  to populate the database.
  
  installwatson
  to enable search feature.
  
  buildwatson
  to create search indexing.

Set environment variables on server, specifically:
  GUIDEBOX_KEY
  to provide information on where to watch movies.

To populate the Movie table of the horrorshow db, runserver and go to /omdb_import, then /guidebox_import

To create Collection records, you must runserver and go to the admin panel until the create collection functionality is implemented.
