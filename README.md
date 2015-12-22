[![Coverage Status](https://coveralls.io/repos/andela-amwaleh/Bucketlist_flask/badge.svg?branch=feature%2Ftest&service=github)](https://coveralls.io/github/andela-amwaleh/Bucketlist_flask?branch=feature%2Ftest)
[![Build Status](https://travis-ci.org/andela-amwaleh/Bucketlist_flask.svg?branch=feature%2Ftest)](https://travis-ci.org/andela-amwaleh/Bucketlist_flask)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/84f92b1d8c8443b29f3306b70b001b4e/badge.svg)](https://www.quantifiedcode.com/app/project/84f92b1d8c8443b29f3306b70b001b4e)

# Introduction
Bucketlist is an API created using Flask Framework 
### Requirements
- Postgres
- Postman

### Installation
- Download the repo
- Download and install [postgres](http://www.postgresql.org/)
- Create two databases in Postgres `flask` and `bucket_test`
  - In the Psql Terminal run :
    - `CREATE DATABASE flask`
    - `CREATE DATABASE bucket_list`
- At the Terminal cd into the project folder and run the following commands 
 * `pip install -r requirements.txt` to install all dependencies
 * `Python manage.py db init`
 * `python manage.py db migrate`
 * `python manage.py db upgrade`
 * `python api/bucketlist.py` to start the server
 

### Endpoints

| End Point                                | Functionality                     |
|------------------------------------------|-----------------------------------|
| POST /auth/login                         | Logs a user in                    |
| POST /api/users                          | Create a user                   |
| ![secure](https://cdn0.iconfinder.com/data/icons/social-messaging-ui-color-shapes/128/lock-circle-green-16.png 'logo') GET /auth/logout                         | Logs a user out                   |
| ![secure](https://cdn0.iconfinder.com/data/icons/social-messaging-ui-color-shapes/128/lock-circle-green-16.png 'logo') POST /bucketlists/                       | Create a new bucket list          |
| ![secure](https://cdn0.iconfinder.com/data/icons/social-messaging-ui-color-shapes/128/lock-circle-green-16.png 'logo') GET /bucketlists/                        | List all the created bucket lists |
| ![secure](https://cdn0.iconfinder.com/data/icons/social-messaging-ui-color-shapes/128/lock-circle-green-16.png 'logo') GET /bucketlists/<id>                    | Get single bucket list            |
|![secure](https://cdn0.iconfinder.com/data/icons/social-messaging-ui-color-shapes/128/lock-circle-green-16.png 'logo') PUT /bucketlists/<id>                    | Update this bucket list           |
| ![secure](https://cdn0.iconfinder.com/data/icons/social-messaging-ui-color-shapes/128/lock-circle-green-16.png 'logo') DELETE /bucketlists/<id>                 | Delete this single bucket list    |
| ![secure](https://cdn0.iconfinder.com/data/icons/social-messaging-ui-color-shapes/128/lock-circle-green-16.png 'logo') POST /bucketlists/<id>/items/            | Create a new item in bucket list  |
| ![secure](https://cdn0.iconfinder.com/data/icons/social-messaging-ui-color-shapes/128/lock-circle-green-16.png 'logo') PUT /bucketlists/<id>/items/<item_id>    | Update a bucket list item         |
| ![secure](https://cdn0.iconfinder.com/data/icons/social-messaging-ui-color-shapes/128/lock-circle-green-16.png 'logo') DELETE /bucketlists/<id>/items/<item_id> | Delete an item in a bucket list   |
- NB. ![secure](https://cdn0.iconfinder.com/data/icons/social-messaging-ui-color-shapes/128/lock-circle-green-16.png 'logo') Need login or Authorization Token 

### Setting up
- Once the server is runnng, navigate to `http://localhost:5000` using Postman 
- Click the header tab and set the Header to `content_type: application/json`
- Click the body tab and select on the `raw` option 
- We shall be using this section for most of our requests
- Json format will be used in sending and recieving request

### Creating Users

- Using the `POST` Method on Postman 
- Navigate to `http://localhost:5000/api/users`.
- Enter username and password in json format in the textarea :
      - request :  `{ "username":"admin", "password":"12345"}`

      - response :
      ```python
                    {
                     "username": "admin"
                    }
      ```


### Login
- Using `POST` method on the Postman
- Navigate to `http://localhost:5000/auth/login`.
- Enter username and password 
  -   request : `{
                   "username":"admdin",
                    "password":"12345"
                }`
  - response  : 
  ```python
        {
              "token": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ1MDcyNzAxNywiaWF0IjoxNDUwNzI2NDE3fQ.eyJ1aWQiOjJ9.cCwq8u_wXZ8wuw9CN3EwhAn7db9w2t_j0o20sVE7rlE"
               }
  ```
- A token will be returned.
- Copy the value of the token
- click on the header and add a key called `token` and paste the copied token in to the value field
- This token will be used to access all the necesary endpoints til it expires
- A token will last for not more than 10 minutes
- Note: Authentication relies on the token all other pages can only be accessed once a valid token is presented


### Adding Bucketlist
- Navigate to `http://localhost:5000/bucketlists`.
- Set request method to `POST`
- make sure the token is set in the Header if you have logged in 
- Enter name of the bucketlist in the textarea and click send
    - request : ``` { "name": "Bucketlist1" }```
    - response :
    ```
                    {
                      "Bucketlist": [
                        [
                          "bucketlist 1",
                          2
                        ]
                      ]
                    }
    ```

### Editing Bucketlist
- Navigate to `http://localhost:5000/bucketlists/<id>,`.
- Set request method to `PUT`
- make sure the token is set in the Header if you have logged in
- You can update the `name`  field which the id provided belongs 
    - request : `{"name":"digger"}`
    - response : `{ "Bucketlist": [ [ "digger" ] ] }`

### Deleting Bucketlist
- Navigate to `http://localhost:5000/bucketlists/<id>,`.
- Set request method to `DELETE`
- replace `<id>` with id you want to delete
- click send

### Adding Item
-  Navigate to `http://localhost:5000/bucketlists/<id>/items`.
-  Replace `<id>` with id of bucketlist you want to add item to 
- Set request method to `POST`
  - request : `{"name":"buy equipment"}`
  - response :
  ```python
    {
    "Bucketlist": [
      {
        "name": "digger",
        "items": [
          {
            "date_created": "Mon, 21 Dec 2015 23:15:09 GMT",
            "date_modified": "Mon, 21 Dec 2015 23:15:09 GMT",
            "done": false,
            "id": 3,
            "name": "buy equipment"
          }
        ],
        "created_by": 2,
        "created_on": "Mon, 21 Dec 2015 22:51:26 GMT",
        "modified_on": "Mon, 21 Dec 2015 23:04:14 GMT",
        "id": 2
      }
    ]
  }
```
- To view all  items in a bucket list set method to `GET`
- navigate to `http://localhost:5000/bucketlists/<id>/items`.

### Editing or Deleteing an Item 

- To Edit :
    - Navigate to `http://localhost:5000/bucketlists/<id>/item/<item_id>`.
    - Set request method to `put `
    - replace `<id>` with id of bucketlist and `<item_id>` with the id of item you want to edit
      *   send a request containing either `name` or `done` fields
      *   request : `{"done":"True"}`
      *   response :
      ```python 
            {
              "items": [
                {
                  "done": true,
                  "name": "buy equipment"
                }
              ]
            }
      ```
- To Delete 
    - Navigate to `http://localhost:5000/bucketlists/<id>/item/<item_id>`.
    - Set request method to `DELETE `
    - replace `<id>` with id of bucketlist and `<item_id>` with the id of item you want to edit
    - Send request
    
### Tests
- To run test use any of the following commands
    * `coverage run --omit="*env*","migrations*","static","templates","test*" -m unittest discover tests`
    * `python -m unittest discover tests`
    * `python tests/test_bucketlist.py`
