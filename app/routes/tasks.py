from fastapi import APIRouter, HTTPException, Query
from typing import List, Union, Optional
from app.schemas import TaskUpdate
from app.lib.db import supabase
from datetime import datetime
from uuid import uuid4

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/")
async def list_tasks(project_id: Optional[str] = Query(None)):
    """
    Return all tasks, or only tasks belonging to a specific project if project_id is provided.
    Example:
      /tasks/            -> all tasks
      /tasks/?project_id=<uuid>  -> only that project
    """
    query = supabase.table("tasks").select("*").order("created_at", desc=True)
    if project_id:
        query = query.eq("project_id", project_id)
    res = query.execute()
    return {"tasks": res.data or []}


@router.post("/")
async def create_tasks(payload: Union[dict, List[dict]]):
    rows = payload if isinstance(payload, list) else [payload]

    normalized = []
    for r in rows:
        if not r.get("text"):
            raise HTTPException(400, "Field 'text' is required")
        normalized.append(
            {
                "id": r.get("id") or str(uuid4()),
                "text": r["text"].strip(),
                "status": r.get("status", "pending"),
                "priority": r.get("priority"),
                "tags": r.get("tags", []),
                "project_id": r.get("project_id"),  # ✅ keep linking tasks
                "created_at": r.get("created_at") or datetime.utcnow().isoformat(),
            }
        )

    res = supabase.table("tasks").insert(normalized).execute()
    return {"tasks": res.data or [], "count": len(res.data or [])}


@router.patch("/{task_id}")
async def update_task(task_id: str, update: TaskUpdate):
    updates = {k: v for k, v in update.dict().items() if v is not None}
    if not updates:
        return {"ok": True}

    res = supabase.table("tasks").update(updates).eq("id", task_id).execute()
    if res.data == []:
        raise HTTPException(404, "Task not found")
    return {"ok": True, "updated": res.data}


@router.delete("/{task_id}")
async def delete_task(task_id: str):
    res = supabase.table("tasks").delete().eq("id", task_id).execute()
    return {"ok": True, "deleted": len(res.data or [])}
