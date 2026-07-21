from datetime import datetime

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    index_exists: bool
    node_count: int
    last_built: datetime | None
    embedding_model: str
    llm_model: str
