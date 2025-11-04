from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4
from datetime import datetime


class Task(BaseModel):
    id: str = str(uuid4())
    text: str
    status: str = "pending"  # "pending" | "completed"
    priority: Optional[str] = None  # (High | Medium | Low)
    tags: Optional[List[str]] = []
    createdAt: str = datetime.utcnow().isoformat()


class TranscriptRequest(BaseModel):
    transcript: str
    with_priority: Optional[bool] = True


class TaskUpdate(BaseModel):
    status: Optional[str] = None
    text: Optional[str] = None
    priority: Optional[str] = None
