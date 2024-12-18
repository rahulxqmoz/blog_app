# Blog Platform Backend

This is the backend of the Blog Platform application, built using Django REST Framework. It provides APIs for user authentication, registration, and blog post management.

---

## Features

- User registration and authentication with JWT (JSON Web Tokens).
- API endpoints for creating, reading, updating, and deleting blog posts.
- Media file handling for uploaded content.
- Modular and scalable architecture.

---

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL
- A virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd blog_platform

**Create a virtual environment**
python -m venv blogenv
source blogenv/bin/activate  # Linux/Mac
blogenv\Scripts\activate     # Windows

**Install dependencies**

pip install -r requirements.txt
Set up .env file: Create a .env file in the root directory and add the following variables:


SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_NAME=blogapp
DATABASE_USER=postgres
DATABASE_PASSWORD=your-db-password
DATABASE_HOST=localhost
DATABASE_PORT=5432
ALLOWED_HOSTS=localhost,127.0.0.1

**Apply migrations**
python manage.py migrate

Run the development server:
python manage.py runserver

**API Endpoints**
Authentication
Register: POST /api/register/
Login: POST /api/login/
Obtain Token: POST /api/token/
Refresh Token: POST /api/token/refresh/
Blog Post Management
List/Create Posts: GET/POST /api/posts/
Retrieve/Update/Delete Post: GET/PUT/DELETE /api/posts/<id>/


**Environment Variables**
The project uses python-decouple to manage environment variables. Secure credentials and sensitive settings are stored in the .env file.

**Deployment**
Set DEBUG=False in .env.
Configure your production database credentials in the .env file.
Use a WSGI server like Gunicorn for deployment.
Set up a secure hosting environment (e.g., AWS, Heroku, or DigitalOcean).

**License**
This project is licensed under the MIT License.


Replace `<repository-url>` with the URL of your repository. This `README.md` provides a comprehensive overview of your backend, URL configurations, and deployment guidelines.






