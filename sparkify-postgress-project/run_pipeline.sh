#!/bin/bash

echo "running create_tables.py to setup sparkify database..."
python create_tables.py

echo "running etl process..."
python etl.py
echo "Done"
