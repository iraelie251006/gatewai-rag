from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        max_length=1000,
        description="User question"
    )

    top_k: int = Field(
        default=3,
        ge=1,
        le=20,
        description="Number of retrieved chunks"
    )
