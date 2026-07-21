from pydantic import BaseModel

class Source(BaseModel):
    document: str
    page: int | None = None
    chunk_id: str
    score: float
    text: str
