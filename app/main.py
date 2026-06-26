from fastapi import FastAPI
from app.db.database import engine, Base

# Import your routers
from app.routers.auth import router as auth_router
from app.routers.task import router as task_router

app = FastAPI(title="To-Do App")

# Hook up the routers
app.include_router(auth_router)
app.include_router(task_router)

@app.get("/")
async def root():
    return {"message": "To-Do App"}

@app.get("/about")
async def about():
    return {"message": "This is a to do app to manage your tasks"}