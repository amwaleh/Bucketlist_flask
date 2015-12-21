[![Coverage Status](https://coveralls.io/repos/andela-amwaleh/Bucketlist_flask/badge.svg?branch=feature%2Ftest&service=github)](https://coveralls.io/github/andela-amwaleh/Bucketlist_flask?branch=feature%2Ftest)
[![Build Status](https://travis-ci.org/andela-amwaleh/Bucketlist_flask.svg?branch=feature%2Ftest)](https://travis-ci.org/andela-amwaleh/Bucketlist_flask)

#INTRODUCTION:
Bucketlist is an API created using Flask Framework 
# Requirements
- postgres
- Postman

# INSTALLATION
- Download the repo
- Download and install [postgres](http://www.postgresql.org/)
- Create two databases in Postgres `flask` and `bucket_test`
  - In the Psql Terminal run :
    - `CREATE DATABASE flask`
    - `CREATE DATABASE bucket_list`
- At the Terminal cd into the project folder and run the following commands 
 - `pip install -r requirements.txt` to install all dependencies
 - `Python manage.py db init`
 - `python manage.py db migrate`
 - `python manage.py db upgrade`
 - `python api/bucketlist.py` to start the server
 
# FEATURES
- Supports multiple users
- Token based authentication
- Users can create multiple bucket lists and bucketlist items
- Users can delete bucket lists and items in them
