# ✅ To-Do API

A production-structured REST API built with **FastAPI**, featuring JWT authentication, layered architecture, and database migrations. Built as a learning project to practice real-world backend patterns — not just a `main.py` dump.

---

## 🏗️ Architecture

```
app/
├── core/
│   └── dependencies.py       # Reusable FastAPI dependencies (get_current_user)
├── db/
│   ├── database.py           # SQLAlchemy engine, session, Base
│   └── models/
│       ├── user.py           # Users ORM model
│       └── task.py           # Tasks ORM model
├── models/
│   ├── user.py               # Pydantic schemas (UserCreate, UserResponse, etc.)
│   └── task.py               # Pydantic schemas (Task, TaskUpdate, TaskResponse)
├── routers/
│   ├── auth.py               # /auth routes
│   └── task.py               # /tasks routes
├── services/
│   ├── auth_service.py       # JWT encode/decode, bcrypt hashing
│   ├── user_service.py       # Register, login business logic
│   └── task_service.py       # Task CRUD business logic
└── main.py                   # App entrypoint, router registration
alembic/                      # Migration files
```

> **Routers are thin.** All business logic lives in services. Routers just bind URLs to functions and declare `response_model`.

---

## 🚀 Features

- **JWT Authentication** — register, login, protected routes via `OAuth2PasswordBearer`
- **Full Task CRUD** — create, read, update, delete tasks
- **Filtering** — by category, status, and deadline
- **Response Models** — strict Pydantic output schemas, no field leakage
- **Database Migrations** — Alembic for schema evolution without data loss
- **Password Security** — bcrypt hashing via `passlib`

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| ORM | SQLAlchemy 2.0 (Mapped / mapped_column) |
| Database | SQLite (via Alembic migrations) |
| Auth | JWT (python-jose) + bcrypt |
| Validation | Pydantic v2 |
| Migrations | Alembic |

---

## ⚡ Getting Started

### 1. Clone and set up environment

```bash
git clone https://github.com/Sudhanshukumar0007/todo-api
cd todo-api
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Mac/Linux
pip install -r requirements.txt
```

### 2. Run migrations

```bash
alembic upgrade head
```

### 3. Start the server

```bash
uvicorn app.main:app --reload
```

### 4. Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

### Auth
| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and get JWT token |

### Tasks (🔒 JWT required)
| Method | Endpoint | Description |
|---|---|---|
| GET | `/tasks/` | Get all tasks for current user |
| POST | `/tasks/` | Create a new task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |
| GET | `/tasks/category/{category}` | Filter tasks by category |
| GET | `/tasks/status/{status}` | Filter tasks by status |
| GET | `/tasks/deadline/{deadline}` | Get tasks before a deadline |

---

## 🔒 Authentication Flow

1. Register via `POST /auth/register`
2. Login via `POST /auth/login` → get `access_token`
3. Click **Authorize** in Swagger UI and paste the token
4. All `/tasks/` routes are now accessible

---

## 📋 Task Schema

```json
{
  "title": "Study Physics",
  "category": "Learning",
  "deadline": "2026-06-30",
  "status": "Ongoing",
  "priority": "High"
}
```

**Category options:** `Mindfulness`, `Daily chores`, `Productive`, `Learning`, `Physical`

**Status options:** `Completed`, `Ongoing`, `Pending`

---

## 🗄️ Database Migrations (Alembic)

```bash
# Apply all migrations
alembic upgrade head

# Check current migration
alembic current

# View migration history
alembic history

# Undo last migration
alembic downgrade -1
```

---

## 📁 Key Design Decisions

- **Services own the logic** — routers never touch the DB directly
- **`response_model` on every route** — API output is always predictable and safe
- **Alembic over `create_all`** — schema changes are versioned and reversible
- **`model_dump(exclude_unset=True)` for PATCH-style updates** — only provided fields are updated

---

## 🔭 Roadmap

- [ ] pytest test suite
- [ ] Docker + docker-compose
- [ ] PostgreSQL support
- [ ] Async SQLAlchemy (AsyncSession + asyncpg)
- [ ] Rate limiting

---

*Built by [Sudhanshu Kumar](https://github.com/Sudhanshukumar0007) — B.Tech CSE (AI/ML), KIET Group of Institutions*
