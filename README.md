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
 

# ENDPOINTS

| End Point                                | Functionality                     |
|------------------------------------------|-----------------------------------|
| POST /auth/login                         | Logs a user in                    |
| POST /api/users                          | Create a user                   |
| *GET /auth/logout                         | Logs a user out                   |
| *POST /bucketlists/                       | Create a new bucket list          |
| *GET /bucketlists/                        | List all the created bucket lists |
| *GET /bucketlists/<id>                    | Get single bucket list            |
| *PUT /bucketlists/<id>                    | Update this bucket list           |
| *DELETE /bucketlists/<id>                 | Delete this single bucket list    |
| *POST /bucketlists/<id>/items/            | Create a new item in bucket list  |
| *PUT /bucketlists/<id>/items/<item_id>    | Update a bucket list item         |
| *DELETE /bucketlists/<id>/items/<item_id> | Delete an item in a bucket list   |
- NB. * Need login or Authorization Token 

## SETTING UP 
- Once the server is runnng, navigate to `http://localhost:5000` using Postman 
- Click the header tab and set the Header to `content_type: application/jason`
- Click the body tab and select on the `raw` option 
- We shall be using this section for most of our requests
- Json format will be used in sending and recieving request

## Creating Users

- Using the `POST` Method on postman 
- Navigate to `http://localhost:5000/api/users`.
- Enter username and password in json format in the textarea :
      - request :  `{ "username":"admin", "password":"12345"}`

      - response :` {
                     "username": "admin"
                    }`
## LOGIN
- Using `POST` method on the postman
- Navigate to `http://localhost:5000/auth/login`.
- Enter username and password 
  -   request : `{
                   "username":"admdin",
                    "password":"12345"
                }`
- response  : `{
              "token": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ1MDcyNzAxNywiaWF0IjoxNDUwNzI2NDE3fQ.eyJ1aWQiOjJ9.cCwq8u_wXZ8wuw9CN3EwhAn7db9w2t_j0o20sVE7rlE"
               }`

              
