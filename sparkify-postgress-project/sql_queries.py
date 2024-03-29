# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS song_play"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
        CREATE TABLE IF NOT EXISTS song_play ( 
                songplay_id SERIAL, 
                start_time timestamp, 
                user_id varchar NOT NULL, 
                level varchar NOT NULL, 
                song_id varchar, 
                artist_id varchar, 
                session_id int NOT NULL, 
                location varchar, 
                user_agent varchar,
                PRIMARY KEY(songplay_id)
                );
        """)

user_table_create = ("""
        CREATE TABLE IF NOT EXISTS users (
                user_id varchar NOT NULL,  
                first_name varchar, 
                last_name varchar, 
                gender varchar, 
                level varchar NOT NULL,
                PRIMARY KEY(user_id)
                );
        """)

song_table_create = ("""
        CREATE TABLE IF NOT EXISTS songs (
                song_id varchar NOT NULL,
                title varchar, 
                artist_id varchar, 
                year int CHECK (year >= 0), 
                duration float,
                PRIMARY KEY(song_id)
                );
        """)

artist_table_create = ("""
        CREATE TABLE IF NOT EXISTS artists (
                artist_id varchar NOT NULL, 
                name varchar, 
                location varchar, 
                latitude DECIMAL(9,6), 
                longitude DECIMAL(9,6),
                PRIMARY KEY(artist_id)
                );
        """)

time_table_create = ("""
        CREATE TABLE IF NOT EXISTS time (
                start_time timestamp NOT NULL, 
                hour int NOT NULL CHECK (hour >= 0),
                day int NOT NULL CHECK (day >= 0), 
                week int NOT NULL CHECK (week >= 0), 
                month int NOT NULL CHECK (month >= 0), 
                year int NOT NULL CHECK (year >= 0), 
                weekday varchar NOT NULL,
                PRIMARY KEY(start_time)
                );
        """)

# INSERT RECORDS
songplay_table_insert = ("""
        INSERT INTO song_play (
                start_time, 
                user_id, 
                level, 
                song_id, 
                artist_id, 
                session_id, 
                location, 
                user_agent) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT DO NOTHING;
        """)

user_table_insert = ("""
        INSERT INTO users(
                user_id, 
                first_name, 
                last_name, 
                gender, 
                level) 
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (user_id) 
                DO UPDATE 
                SET level = EXCLUDED.level;
        """)

song_table_insert = ("""
        INSERT INTO songs (
                song_id, 
                title, 
                artist_id, 
                year, 
                duration) 
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT DO NOTHING;
        """)

artist_table_insert = ("""
        INSERT INTO artists (
                artist_id, 
                name, 
                location, 
                latitude, 
                longitude) 
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT DO NOTHING;
        """)

time_table_insert = ("""
        INSERT INTO time (
                start_time, 
                hour, 
                day, 
                week, 
                month, 
                year, 
                weekday) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT DO NOTHING;
        """)

# FIND SONGS
song_select = ("""
        SELECT songs.song_id, artists.artist_id 
                FROM (songs JOIN artists ON songs.artist_id = artists.artist_id);
        """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]