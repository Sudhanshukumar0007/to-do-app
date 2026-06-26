from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated, Literal
from datetime import date

CategoryType = Literal["Mindfulness", "Daily chores", "Productive", "Learning", "Physical"]
StatusType = Literal["Completed", "Ongoing", "Pending"]

class Task(BaseModel):
    title: Annotated[str, Field(..., description="Title of the task", examples=["Study Physics"])]
    category: Annotated[CategoryType, Field(..., description="Category of the task", examples=["Mindfulness"])]
    deadline: Annotated[date, Field(..., description="Deadline of the task in yyyy-mm-dd format", examples=["2026-06-23"])]
    status: Annotated[StatusType, Field(..., description="Current status of the task", examples=["Completed"])]
    priority:Annotated[str,Field(...,description="Priority of the task",examples=["First"])]

class TaskUpdate(BaseModel):
    title: str | None = None
    category: CategoryType | None = None
    deadline: date | None = None
    status: StatusType | None = None
    priority: str | None = None
# In your task model
class TaskResponse(BaseModel):
    id: int
    title: str
    category: str
    deadline: date
    status: str
    priority:str 

    model_config = ConfigDict(from_attributes=True)