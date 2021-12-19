# Database Security
A repository for learning to secure a MongoDB database

# Objectives
• Create a MongoDB database which would contain some secured sensitive data (protected
via 2-way encryption);
• Create an application which would display the data contained in the database (both
common data and the decrypted sensitive data);
• Make sure that the sensitive data can only be accessed via your application (i.e. it is
secure).

# Implementation

## Step 1
To run the program it is mandatory to create a key to secure the database:
```
python3 path/to/file/create_key.py
```

## Step 2
Fill the database with data, running:
```
python3 path/to/file/create_database.py
```
## Step 3
Run the application:
```
python3 path/to/file/gui.py
```
## Step 4
Connect to the database by clicking: `Connect to Database` button, then introduce the username and password of the user that is registred in the created MongoDB database. And then press button `View data` that will display all the data decripted.

## Step 5 
`File -> Log out`

## Step 6
`File -> Exit`