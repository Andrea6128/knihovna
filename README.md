# knihovna
Little web based on Django that shows a book library and whether a book is currently borrowed.

# requirements
- Python 3.8.1
- Django 3.0.2
- psycopg2 2.8.4
- PostgreSQL db

# install
- install PostgreSQL from their website
- create a password and create a new database 'knihovna', make sure the db server is running
- add path to the PostgreSQL installed binaries to PATH
- install Python
- install venv and activate it
- install required modules: pip install -r requirements.txt 
- migrate db: python3 manage.py migrate
- cerate superuser: python3 manage.py createsuperuser

# run
- run server: python3 manage.py runserver
- go to http://127.0.0.1:8000/admin, enter superuser credentials
- fill or modify the database using admin interface
- check out http://127.0.0.1:8000/ for result
