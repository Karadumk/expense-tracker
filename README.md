# Expense Tracker API

A simple FastAPI-based backend for tracking your expenses. Users can register, log in, and manage their own set of expenses categorized by type and date.

## ✨ Features

- User authentication (Sign up & Login)
- JWT-based protected routes
- Create, read, update, delete expenses
- Filter expenses by:
  - Past week
  - Past month
  - Last 3 months
  - Custom date range
- Categories: Groceries, Leisure, Electronics, Utilities, Clothing, Health, Others

## 🛠 Tech Stack

- **Backend**: Python, FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Auth**: JWT via python-jose

## 📁 Project Structure
```
expense-tracker/
├── app/
│   ├── main.py # FastAPI app entry point
│   ├── models.py  # SQLAlchemy models
│   ├── schemas.py # Pydantic schemas
│   ├── database.py # DB config & session 
│   ├── auth.py # Auth logic (hashing, JWT)
│   ├── crud.py # DB queries and logic
│   └── routers/
│       ├── users.py # Routes for signup/login
│       └── expenses.py # Routes for managing expenses
├── .env
├── requirements.txt
└── alembic/
```

## 🚀 Getting Started

1. Clone the repo
2. Install dependencies
3. Run the app

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 📌 To-Do

- [ ] Signup & Login
- [ ] JWT Auth
- [ ] Expense CRUD
- [ ] Filtering endpoints
- [ ] DB migrations (optional)
- [ ] Tests
