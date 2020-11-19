# DROP TABLES IF THEY ALREADY EXIST

user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"

# CREATE TABLES
# SONGPLAYS TABLE IS THE FACT TABLE WITH FOREIGN KEY REFERENCES TO OTHER TABLES

user_table_create = ("""
CREATE TABLE users(
user_id INTEGER PRIMARY KEY NOT NULL,
firstName VARCHAR(255),
lastName VARCHAR(255),
gender VARCHAR(1),
level VARCHAR(50))
""")

song_table_create = ("""
CREATE TABLE songs(
song_id VARCHAR(100) PRIMARY KEY NOT NULL,
title VARCHAR(255),
artist_id VARCHAR(100),
year INTEGER,
duration REAL)
""")

artist_table_create = ("""
CREATE TABLE artists(
artist_id VARCHAR(100) PRIMARY KEY NOT NULL,
name VARCHAR(255),
location VARCHAR(255),
latitude REAL,
longitude REAL)
""")

time_table_create = ("""
CREATE TABLE time(
start_time TIMESTAMP PRIMARY KEY NOT NULL,
hour INTEGER,
day INTEGER,
week INTEGER,
month INTEGER,
year INTEGER,
weekday INTEGER)
""")

songplay_table_create = ("""
CREATE TABLE songplays(
songplay_id SERIAL PRIMARY KEY NOT NULL,
start_time TIMESTAMP REFERENCES time(start_time) NOT NULL,
user_id VARCHAR(100) REFERENCES users(user_id) NOT NULL,
level VARCHAR(100),
song_id VARCHAR(100) REFERENCES songs(song_id) NOT NULL,
artist_id VARCHAR(100) REFERENCES artists(artist_id) NOT NULL,
session_id NUMERIC,
location VARCHAR(255),
user_agent TEXT)
""")

# INSERT RECORDS INTO TABLES

user_table_insert = ("""INSERT INTO users(user_id, firstName, lastName, gender, level) VALUES (%s, %s, %s, %s, %s) 
ON CONFLICT (user_id) DO UPDATE SET level=users.level """)

song_table_insert = ("""INSERT INTO songs(song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO DO NOTHING """)

artist_table_insert = ("""INSERT INTO artists(artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING """)


time_table_insert = ("""INSERT INTO time(start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING """)

songplay_table_insert = ("""INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """)


# FIND SONGS

# FIND SONG BY SONG ID AND ARTIST ID
song_by_songid_artistid = ("""SELECT s.song_id, a.artist_id FROM songs s, artists a WHERE s.artist_id = a.artist_id AND s.title = %s AND a.name = %s AND s.duration = %s""")


# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [user_table_drop, song_table_drop, artist_table_drop, time_table_drop, songplay_table_drop]