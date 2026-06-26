# To-Do API

A REST API built with FastAPI that I wrote to learn how real backends are structured — not just how to make endpoints work, but how to organize code so it doesn't become a mess when it grows.

 This one separates concerns properly: routers handle HTTP, services handle logic, models handle data. Each layer only knows what it needs to know.

---

## Architecture

```
app/
├── core/
│   └── dependencies.py       # get_current_user — used across all protected routes
├── db/
│   ├── database.py           # engine, session, Base
│   └── models/
│       ├── user.py           # Users table
│       └── task.py           # Tasks table
├── models/
│   ├── user.py               # Pydantic schemas for users
│   └── task.py               # Pydantic schemas for tasks
├── routers/
│   ├── auth.py               # /auth routes
│   └── task.py               # /tasks routes
├── services/
│   ├── auth_service.py       # JWT + bcrypt
│   ├── user_service.py       # register, login
│   └── task_service.py       # task CRUD
└── main.py                   # app entry point, router registration
alembic/                      # migration history
```

Routers are thin — they bind URLs to service functions and declare `response_model`. That's it. No DB calls, no business logic.

---

## Tech Stack

| | |
|---|---|
| Framework | FastAPI |
| ORM | SQLAlchemy 2.0 |
| Database | PostgreSQL (via Docker) |
| Auth | JWT (python-jose) + bcrypt |
| Validation | Pydantic v2 |
| Migrations | Alembic |
| Tests | pytest + httpx |
| Containerization | Docker + docker-compose |

---

## Getting Started

Clone the repo and make sure Docker Desktop is running.

```bash
git clone https://github.com/Sudhanshukumar0007/to-do-app.git
cd to-do-app
cp .env.example .env
```

Edit `.env` with your values, then:

```bash
docker-compose up --build
```

That's it. Docker spins up the API and PostgreSQL, runs Alembic migrations, and starts the server. No manual setup.

Open `http://127.0.0.1:8000/docs` to explore the API.

---

## API

### Auth
| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Create an account |
| POST | `/auth/login` | Get a JWT token |

### Tasks (JWT required)
| Method | Endpoint | Description |
|---|---|---|
| GET | `/tasks/` | All tasks for the current user |
| POST | `/tasks/` | Create a task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |
| GET | `/tasks/category/{category}` | Filter by category |
| GET | `/tasks/status/{status}` | Filter by status |
| GET | `/tasks/deadline/{deadline}` | Tasks before a deadline |

To use protected routes in Swagger: login → copy the token → click Authorize → paste it.

---

## Task Schema

```json
{
  "title": "Study Physics",
  "category": "Learning",
  "deadline": "2026-06-30",
  "status": "Ongoing",
  "priority": "High"
}
```

Category options: `Mindfulness`, `Daily chores`, `Productive`, `Learning`, `Physical`

Status options: `Completed`, `Ongoing`, `Pending`

---

## Running Tests

```bash
pytest tests/ -v
```

Tests use a separate SQLite database so they never touch your real data. Auth and all task endpoints are covered.

---

## Migrations

```bash
alembic upgrade head      # apply all pending migrations
alembic current           # see where the DB is
alembic history           # full migration log
alembic downgrade -1      # roll back one migration
```

Schema changes go through Alembic — no `create_all()` in production code.

---

## What I learned building this

- How to structure a FastAPI project so it doesn't collapse when you add features
- Why `response_model` matters — without it, internal DB fields leak into API responses
- How Alembic migrations work and why `create_all()` isn't enough for real projects
- How Docker Compose connects services — the API container talks to the PostgreSQL container by service name, not localhost
- Writing tests that override dependencies so they never touch the real database

---

## Roadmap

- [x] pytest test suite
- [x] Docker + docker-compose
- [x] PostgreSQL
- [ ] Async SQLAlchemy (AsyncSession + asyncpg)
- [ ] Rate limiting

---

Built by [Sudhanshu Kumar](https://github.com/Sudhanshukumar0007) — B.Tech CSE (AI), KIET Group of Institutions
