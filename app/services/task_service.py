# what functions we have to write:- 
# get all task
# get task by catergories
# Create new Task
# update task
# delete task
# get task by status
# get task within deadline
from fastapi import HTTPException,Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models.task import Tasks
from app.db.models.user import Users
from app.core.dependencies import get_current_user
from app.models.task import Task,TaskUpdate
from datetime import date
async def get_tasks(db:Session=Depends(get_db),user:Users=Depends(get_current_user)):
    tasks = db.query(Tasks).filter(Tasks.user_id==user.id).all()
    return tasks
async def get_tasks_by_category(category:str,db:Session=Depends(get_db),user:Users=Depends(get_current_user)):
    tasks = db.query(Tasks).filter(Tasks.user_id==user.id,Tasks.category==category).all()
    return tasks
async def create_new_task(task:Task,db:Session=Depends(get_db),user:Users=Depends(get_current_user)):
    task_db = Tasks(
        user_id = user.id,
        title = task.title,
        category = task.category,
        deadline = task.deadline,
        status = task.status,
        priority = task.priority
    )
    db.add(task_db)
    db.commit()
    db.refresh(task_db)

    return task_db
async def update_task(task_id:int,task:TaskUpdate,db:Session=Depends(get_db),user:Users=Depends(get_current_user)):
    task_db = db.query(Tasks).filter(Tasks.id==task_id,Tasks.user_id==user.id).first()
    if not task_db:
        raise HTTPException(status_code=404,detail="Task Does not exist")
    updated_task = task.model_dump(exclude_unset = True)
    for key,val in updated_task.items():
        setattr(task_db,key,val)
    db.commit()
    db.refresh(task_db)
    return task_db
async def delete_task(task_id:int,db:Session=Depends(get_db),user:Users=Depends(get_current_user)):
    task = db.query(Tasks).filter(Tasks.id==task_id,Tasks.user_id==user.id).first()
    if not task:
        raise HTTPException(status_code=404,detail="Tasks does not exist")
    db.delete(task)
    db.commit()
    return task
async def get_task_by_status(status:str,db:Session=Depends(get_db),user:Users=Depends(get_current_user)):
    tasks = db.query(Tasks).filter(Tasks.status==status,Tasks.user_id==user.id).all()
    return tasks
async def get_task_before_deadline(deadline:date,db:Session=Depends(get_db),user:Users=Depends(get_current_user)):
    tasks = db.query(Tasks).filter(Tasks.deadline<deadline,Tasks.user_id==user.id).all()
    return tasks