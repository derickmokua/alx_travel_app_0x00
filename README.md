# ALX Travel App 🌍✈️

A scalable Django REST API project designed for listing travel experiences and destinations. This project is part of the ALX Software Engineering track and focuses on best practices in backend setup, database integration, and API documentation.

---

## 🚀 Project Overview

The `alx_travel_app` is a real-world Django application built to serve as the foundation for a travel listing platform. This milestone includes:

- **Django REST API setup**
- **MySQL database configuration**
- **Environment variable management**
- **CORS support**
- **Swagger documentation**
- **Celery and RabbitMQ setup (for future background tasks)**

---

## 📁 Project Structure

alx_travel_app/
├── alx_travel_app/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── listings/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── views.py
│ └── migrations/
├── requirements.txt
├── manage.py
├── .env
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/alx_travel_app.git
cd alx_travel_app
2. Create a Virtual Environment

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file in the root directory:

DEBUG=True
SECRET_KEY=your_secret_key_here
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306

5. Run Migrations

python manage.py migrate

6. Start the Development Server

python manage.py runserver

🧪 API Testing

Visit the Swagger API documentation:

    http://127.0.0.1:8000/swagger/

✅ Tech Stack

    Backend: Django, Django REST Framework

    Database: MySQL

    API Docs: Swagger (drf-yasg)

    Async Tasks: Celery & RabbitMQ (future integration)

    CORS: django-cors-headers

    Env Config: django-environ

🤝 Author

Derick Mokua
"In code I trust."
📝 License

This project is open-source and available under the MIT License.
