import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from fastapi import FastAPI, HTTPException
from tasks.models import Task
from pydantic import BaseModel, validator
from typing import List, Optional


# Create the Fast API instance
app = FastAPI()

# This is our data model for a task
class TaskSchema(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str

    @validator('status')
    def validate_status(cls, value):
        valid_statuses = ['pending', 'in_progress', 'completed']
        if value not in valid_statuses:
            raise ValueError(f"Status must be one of: {', '.join(valid_statuses)}")
        return value

class Config:
    orm_mode = True

# Initialize our empty list -> Used to test Fast API functionality
## tasks_db = []


# Get endpoint, list all tasks
@app.get("/tasks/", response_model=List[TaskSchema])
def read_tasks():
    tasks = Task.objects.all()
    return list(tasks)

# Post endpoint, create a new task, add it to list of tasks
@app.post("/tasks/", response_model=TaskSchema)
def create_task(task: TaskSchema):
    new_task = Task.objects.create(
        title=task.title,
        description=task.description,
        status=task.status
    )
    return new_task

# Get endpoint, single task
@app.get("/tasks/{task_id}", response_model=TaskSchema)
def read_task(task_id: int):
    try:
        task = Task.objects.get(id=task_id)
        return task
    except Task.DoesNotExist:
        raise HTTPException(status_code=404, detail="Task not found or it doesn't exist")

# Put endpoint, update single task
@app.put("/tasks/{task_id}", response_model=TaskSchema)
def update_task(task_id: int, updated_task: TaskSchema):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        raise HTTPException(status_code=404, detail="Task not found or it doesn't exist")

    task.title = updated_task.title
    task.description = updated_task.description
    task.status = updated_task.status
    task.save()
    return task

# Delete endpoint, delete single task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):      
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        return {"detail": "Task deleted"}
    except Task.DoesNotExist:
        raise HTTPException(status_code=404, detail="Task not found or it doesn't exist")