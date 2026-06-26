from fastapi import APIRouter
# Import your task functions here
from app.models.task import TaskResponse
from app.services.task_service import (
    get_tasks, get_tasks_by_category, create_new_task, 
    update_task, delete_task, get_task_by_status, get_task_before_deadline
)

router = APIRouter(prefix="/tasks", tags=["Tasks"])

router.get("/", response_model=list[TaskResponse])(get_tasks)
router.post("/", response_model=TaskResponse)(create_new_task)
router.put("/{task_id}", response_model=TaskResponse)(update_task)
router.delete("/{task_id}", response_model=TaskResponse)(delete_task)
router.get("/category/{category}", response_model=list[TaskResponse])(get_tasks_by_category)
router.get("/status/{status}", response_model=list[TaskResponse])(get_task_by_status)
router.get("/deadline/{deadline}", response_model=list[TaskResponse])(get_task_before_deadline)