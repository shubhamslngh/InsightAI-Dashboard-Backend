from fastapi import APIRouter, HTTPException
from app.schemas import TranscriptRequest, Task
from app.services.llm_service import generate_tasks
from uuid import uuid4
from datetime import datetime
from app.lib.db import supabase

router = APIRouter(prefix="/generate", tags=["generate"])


@router.post("/")
async def generate_action_items(payload: TranscriptRequest):
    if not payload.transcript or len(payload.transcript) < 10:
        raise HTTPException(status_code=400, detail="Transcript too short")

    tasks_raw = generate_tasks(payload.transcript, payload.with_priority)
    tasks = [
        {
            "text": t.get("text", ""),
            "status": "pending",
            "priority": t.get("priority"),
            "tags": t.get("tags", []),
        }
        for t in tasks_raw
    ]

    supabase.table("tasks").insert(tasks).execute()
    return {"tasks": tasks}
