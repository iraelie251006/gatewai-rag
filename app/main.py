from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import engine, get_db

# Create the tasks.db file and table(s) on startup, if they don't exist yet
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Simple Task API",
    description="A minimal FastAPI app with a GET and a POST endpoint, "
                 "Pydantic validation, and a local SQLite database.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "Task API is running. Visit /docs for interactive API docs."}


@app.post("/tasks", response_model=schemas.TaskResponse, status_code=201)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """Create a new task."""
    new_task = models.Task(
        title=task.title,
        description=task.description,
        completed=task.completed,
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@app.get("/tasks", response_model=list[schemas.TaskResponse])
def list_tasks(db: Session = Depends(get_db)):
    """Get all tasks."""
    return db.query(models.Task).all()


@app.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    """Get a single task by ID."""
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
