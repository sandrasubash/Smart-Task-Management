# Smart Task Management System

A backend-based Smart Task Management System developed using FastAPI.  
The application provides secure authentication, role-based access control, and task management functionalities for Admins, Managers, and Users.

---

## Features

- User Registration & Login
- JWT Authentication
- Role-Based Access Control (Admin, Manager, User)
- Task Creation, Update, Delete, and Tracking
- RESTful API Development
- Database Integration using SQLAlchemy
- API Testing using Swagger UI and Postman

---

## Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite

### Authentication
- JWT Authentication
- Passlib (Password Hashing)

### Tools
- Git
- GitHub
- Postman

---

## Project Structure

```bash
app/
│
├── main.py
├── database.py
│
├── models/
├── schemas/
├── routers/
├── auth/
├── services/
└── utils/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Smart-Task-Management.git
```

### Navigate to Project

```bash
cd Smart-Task-Management
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Server

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

Swagger UI:

```bash
http://127.0.0.1:8000/docs
```

---

## Roles

### Admin
- Manage all users
- Assign managers
- Monitor tasks

### Manager
- Assign tasks to users
- Update task status

### User
- View assigned tasks
- Update progress

---

## Future Enhancements

- PostgreSQL Integration
- Email Notifications
- AWS Deployment
- Docker Support
- Frontend Integration

---

## Author

Sandra Subhash

GitHub:
https://github.com/sandrasubash
