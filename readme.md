# Django Project

<br>

<a href='https://www.aschonnproject.com'>Django Project Link</a>

<br>

# Motivation:
To compare different frameworks and to see which would give me the best result. I figured the best way to test this out would be to create identical Applications using those both frameworks.

<br>

# Dependencies:
- I used python 3.8.2 but anything over 3.7 will work.
- All the related dependencies are in the requirements.txt

<br>

# Required Knowledge:
- Django (Framework) 
- Python (Language)
- SQLAlchemy (translater)
- Gunicorn (Web Server)
- Heroku (Server)
- Postgresql (Database)  

<br>

# SPECIAL FEATURES:
- Authentication: Password Hashing, Password Reset, Login
- Python Instantiated Forms for Adding, Updating, and Deleting Posts
- Mail
- Pagination
- Responsive Design Using Bootstrap
- Error Handlers and Flash Messages
- Picture Hexing and Resizing 
- Admin GUI
- Easy Database Setup
- Simple Email Setup (from django.core.mail import send_mail....more at users/views.py)

<br>

# How to run:

## Virtual Env:
    1) Install dependency: 
        
            pip install virtualenv

    2) Create Virtualenv :

            virtualenv -p /usr/bin/python3 env

    3) Activate Virtualenv : 

            source env/bin/activate

    4) Deactivate : 
            
            deactivate

## ENVIROMENTAL VARIABLES:

    Install python-dotenv:

        $ pip install dotenv

    Create a '.env' file:

        $ touch .env

    Add DATABASE_URL:

        DATABASE_URL = "postgres://{username}:{password}@localhost:{port}/{database_name}"

    Add SECRET_KEY (OPTIONAL):

        SECRET_KEY = "{SECRET_KEY}"

<br>

# Setup database:

## Enter In Database:
1) In the settings.py file enter in credentials for postgresql or sqlite3

## Migration Models/Tables To Database:
1) python manage.py makemigrations
2) python manage.py migrate

## Create a superuser (access admin page):
1) python manage.py createsuperuser
2) Answer all questions


<br>
<br>

# MAIL SETUP:

1) Setup and account (gmail)
2) Create an App Password 
3) enter in your own credentials into settings.py


<br>
<br>

# (MANUALLY) INSERT DATA INTO TABLES:


## ADD MOCK DATA:
        >>> import json
        >>> from blog.models import Post
        >>> with open('posts.json') as f:
        ...     posts_json = json.load(f)
        ... 
        >>> for post in posts_json:
        ...     post = Post(title=post['title'], content=post['content'], author_id=post['user_id'])
        ...     post.save()

<br>
<br>

# Website Setup:


## linode (Linux from scratch)
1) Create an Account
2) Create a linode using favorite Operating System setup
3) Select Server and Click Create
4) More infomation and Instruction:
    https://www.youtube.com/watch?v=goToXTC96Co&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=13

