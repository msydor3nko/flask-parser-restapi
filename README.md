# Flask Parser and RestAPI
The simple mini app based on Python Flask.

### Key features:
- parsing data with products and their reviews from CSV files (datasets attached)
- saving parsed data into PostgreSQL with one-to-many relationships
- getting DB access to product info and reviews with pagination by 'id' using API GET-endpoint (the response cached on 10 sec.)
- creating new product review into DB by product 'id' using API PUT-endpoint


## What do you need

**You need:** Git, Python3, pip, PostgreSQL (or just use SQLite).


## Guides

### Setup environment

* Clone the App repository using Git

`git clone https://github.com/msydor3nko/flask-parser-restapi.git`

* Enter to the 'flask-parser-restapi' directory

`cd flask-parser-restapi`

* Create and activate virtual environment

`python3 -m venv venv`

`source venv/bin/activate`

* Upgrade pip'

`pip install pip -U`

* Install all required libraries from 'requirements.txt'

`pip install -r requirements.txt`

### Datasets parsing 

* run 'parser.py' to parse datasets and save results into database:

`python parser.py`


### API using

* Run Flask app to use API:

`flask run`

* To make requests use endpoints with standard Flask options

GET: `http://127.0.0.1:5000/api/products/<id>`

PUT: `http://127.0.0.1:5000/api/reviews/<id>`


# Note
You need setup PostgreSQL connection in '.env' file to work with data.

You can choose SQLite (using by default) as alternative DB using command:

`flask db init`

Migrations are also available if it needed:

`flask db migrate -m 'init db'`

`flask db upgrade`