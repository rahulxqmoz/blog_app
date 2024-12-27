# Blog App

A blog platform built using Django as the backend framework. This application allows users to register, log in, and create, view, and manage blog posts.

## Features

- User Registration and Login using JWT Authentication
- CRUD operations for blog posts
- Role-based access control (Authenticated users only)
- Secure API endpoints
- CORS support for frontend integration

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.9 or later
- PostgreSQL
- Django 5.1.4
- Node.js (if integrating with a frontend)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rahulxqmoz/blog_app.git
   cd blog_app/backend/blog_platform

## Set up a virtual environment
python -m venv venv
source venv/bin/activate 


## Install the dependencies:
pip install -r requirements.txt

## Configure environment variables:
Create a .env file in the root directory and add:

SECRET_KEY=<your_secret_key>
DEBUG=True
DATABASE_NAME=<your_database_name>
DATABASE_USER=<your_database_user>
DATABASE_PASSWORD=<your_database_password>
DATABASE_HOST=localhost
DATABASE_PORT=5432
ALLOWED_HOSTS=localhost,127.0.0.1

## Set up the database:
python manage.py makemigrations
python manage.py migrate

## Create a superuser (admin):
python manage.py createsuperuser

## Run the server:
python manage.py runserver

## API Endpoints
## Authentication
Register: POST /api/register/
Login: POST /api/login/
Get Token: POST /api/token/
Refresh Token: POST /api/token/refresh/

## Blog Posts
List Posts: GET /api/posts/
Create Post: POST /api/posts/
Update Post: PUT /api/posts/<id>/
Delete Post: DELETE /api/posts/<id>/


## Contributing
Contributions are welcome! Please fork this repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Django Documentation: https://docs.djangoproject.com
Simple JWT: https://django-rest-framework-simplejwt.readthedocs.io

