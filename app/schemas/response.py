from pydantic import BaseModel

from app.models.source import Source

class QueryResponse(BaseModel):
    answer: str
    sources: list[Source]
    retrieved_chunks: int
    response_time_ms: float
