from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    """Schema for creating a task (POST request body)."""
    title: str = Field(..., min_length=1, max_length=100, example="Buy groceries")
    description: str | None = Field(None, max_length=500, example="Milk, eggs, bread")
    completed: bool = False


class TaskResponse(BaseModel):
    """Schema for returning a task (GET response body)."""
    id: int
    title: str
    description: str | None = None
    completed: bool

    class Config:
        from_attributes = True  # allows returning SQLAlchemy objects directly
