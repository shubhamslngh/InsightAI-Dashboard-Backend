from fastapi import APIRouter, HTTPException
from typing import List
from app.lib.db import supabase
from uuid import uuid4
from datetime import datetime

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("/")
async def list_projects():
    """List all saved projects."""
    res = (
        supabase.table("projects").select("*").order("created_at", desc=True).execute()
    )
    return {"projects": res.data or []}


@router.post("/")
async def create_project(name: str):
    """Create a new project if it doesn't exist."""
    name = name.strip()
    if not name:
        raise HTTPException(400, "Project name required")

    existing = supabase.table("projects").select("*").eq("name", name).execute()
    if existing.data:
        return {"project": existing.data[0]}  # return existing project

    res = (
        supabase.table("projects")
        .insert(
            {
                "id": str(uuid4()),
                "name": name,
                "created_at": datetime.utcnow().isoformat(),
            }
        )
        .execute()
    )

    return {"project": res.data[0]}
