# Blog App Backend

Blog App is a minimal yet powerful blogging platform that enables users to create, manage, and engage with blog posts. It ensures secure authentication and seamless frontend integration.

## Features

- **User Authentication**: Secure JWT authentication for user login and registration.
- **Blog Management**: Create, update, delete, and view blog posts.
- **Role-Based Access Control**: Restricts operations based on user roles.
- **Secure API Endpoints**: Protected routes for authenticated users.
- **CORS Support**: Enables seamless frontend integration.

---

## Tech Stack

- **Backend:** Django Rest Framework (DRF)
- **Authentication:** JWT (JSON Web Tokens)
- **Database:** PostgreSQL
- **State Management:** Redux (Frontend Integration)

---

## Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python 3.9+**
- **PostgreSQL**
- **Django 5.1.4**
- **Node.js** (if integrating with a frontend)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/blog_app.git
cd blog_app/backend
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add:

```plaintext
SECRET_KEY=<your_secret_key>
DEBUG=True
DATABASE_NAME=<your_database_name>
DATABASE_USER=<your_database_user>
DATABASE_PASSWORD=<your_database_password>
DATABASE_HOST=localhost
DATABASE_PORT=5432
ALLOWED_HOSTS=localhost,127.0.0.1
```

Replace the placeholders with actual values.

### 5. Set Up the Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 7. Run the Server

```bash
python manage.py runserver
```

The backend will be available at [http://localhost:8000](http://localhost:8000).

---

## API Endpoints

### Authentication

- **Register**: `POST /api/register/`
- **Login**: `POST /api/login/`
- **Get Token**: `POST /api/token/`
- **Refresh Token**: `POST /api/token/refresh/`

### Blog Posts

- **List Posts**: `GET /api/posts/`
- **Create Post**: `POST /api/posts/`
- **Update Post**: `PUT /api/posts/<id>/`
- **Delete Post**: `DELETE /api/posts/<id>/`

---

## Notes

- Ensure the database is correctly configured in the `.env` file.
- Keep your `.env` file private and never push it to a public repository.

---

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Django Documentation](https://docs.djangoproject.com)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io)

