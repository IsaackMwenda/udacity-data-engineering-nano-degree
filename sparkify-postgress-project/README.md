# Project: Data Modeling with Postgres - Sparkify

## Usecase description
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

## Solution
ETL pipeline and Postgres database optimized for songplay analysis.

## Database Schema Design
Schema type: star - Optimized for simple queries and fast reads.
Fact tables: song_play
Dimension Tables: users, songs artists and time. This schema design helps with simplifying complex queries and allows for greater performance when reading data from the database.

## Pipeline File Structure
### sql_queries.py
Contains queries that; drops the tables if they exist, creates the tables, inserts extracted data from the datasets to the tables and a select query that gets the songplay data.

### create_tables.py
Executes the drop and create table queries sql_queries.py file .

### etl.py
Runs the end to end pipeline stages i.e extract data from the json data files and insert into the database.

## Running Pipeline
### Pre-requisites
Install the following tools before running the pipeline:
 - Postgres SQL
 - Bash
 - Python 3.6+
 - psycopg2
 - pandas

To run the pipeline run </br>
```
$ ./run_pipeline.sh
```
