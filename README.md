# Data Modeling with Postgres

## Udacity Project 1

#### Schema for Song Play Analysis

Using the song and log datasets, a star schema has been created and optimized for queries on song play analysis. This includes the following tables.

Fact Table:
songplays - records in log data associated with song plays i.e. records with page NextSong
(songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)

Dimension Tables:
users - users in the app
(user_id, first_name, last_name, gender, level)

songs - songs in music database
(song_id, title, artist_id, year, duration)

artists - artists in music database
(artist_id, name, location, latitude, longitude)

time - timestamps of records in songplays broken down into specific units
(start_time, hour, day, week, month, year, weekday)


#### Project Folder Hierarchy

In addition to the data files, the project workspace includes six files:

test.ipynb: Displays the first few rows of each table to let users check the database.

create_tables.py: Drops and creates your tables. This file should be run to to reset the tables before running the ETL Scripts each time.

etl.ipynb: Reads and processes a single file from song_data and log_data and loads the data into the tables. This notebook contains detailed instructions on the ETL process for each of the tables.

etl.py: Reads and processes files from song_data and log_data and loads them into the tables.

sql_queries.py: Contains all the sql queries, and is imported into the last three files above.



#### Instructions to run the project

Run : python create_tables.py followed by python etl.py

Note: etl.py ran successfully and loaded all datasets as expected.


#### References:

Udacity Data Engineering Video Lectures, cheat sheet. 

https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e
https://chartio.com/resources/tutorials/how-to-list-databases-and-tables-in-postgresql-using-psql/
https://www.postgresqltutorial.com/postgresql-foreign-key/
https://www.postgresqltutorial.com/postgresql-insert/
https://www.postgresql.org/docs/8.0/sql-alteruser.html
https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html
https://stackoverflow.com/questions/1281875/making-sure-that-psycopg2-database-connection-alive
https://dba.stackexchange.com/questions/192897/postgres-relation-does-not-exist-error
https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe.htm





