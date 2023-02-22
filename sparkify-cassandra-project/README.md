# Project: Data Modeling with Cassandra -

## Usecase description
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

## Solution
ETL pipeline and Cassandra database optimized for song listenership queries.

## Database Schema Design
Denormalized tables optimized for queries

## Pipeline File Structure

### etl.pynb
Runs the end to end pipeline stages i.e extract data from the csv data files and insert into the database.

## Running Pipeline
### Pre-requisites
Install the following tools before running the pipeline:
 - cassandra
 - Python 3.6+

To run the pipeline run notebook end to end</br>

