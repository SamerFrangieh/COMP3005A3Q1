# PostgreSQL Python CRUD Application
This repository has a Python application that shows how to perform CRUD operations on a PostgreSQL database using the psycopg2 library. It uses a students table as an example and is used for my assignement 3 in comp3005.

### Before you start, here is my youtube video link :)
https://youtu.be/2-87WvOQfY4?si=Dr7ywdaYfEcalLFd

## Prerequisites
Before you begin, make sure these are installed:

1. PostgreSQL
2. Python 
3. pip (Python package installer)

## Step 1: Install psycopg2
pip install psycopg2-binary

use this command

## Step 2: Database
1. Open pgadmin4 and connect to your server
2. create a database
3. open query tool for the new database you made and execute the code in the txt 
   file i provided to create and populate table

## Step 3: Configure software
Fill in the conn variable with your imformation to connect to the database

conn = psycopg2.connect(
    dbname='dbname', 
    user='your_username', 
    password='your_password', 
    host='localhost'
)


## Step 4: Run the application

python <YOUR_SCRIPT>.py

this will make the changes for you

