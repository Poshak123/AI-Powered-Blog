from fastapi import APIRouter, HTTPException
from app.database import db
from app.schemas.blog import BlogCreate, BlogOut, BlogUpdate
from datetime import datetime
from bson import ObjectId
from typing import List
import asyncio
import re

router = APIRouter()

def slugify(text: str) -> str:
    s = re.sub(r"[^\w\s-]", "", text).strip().lower()
    s = re.sub(r"[-\s]+", "-", s)
    return s

@router.post("/", response_model=dict)
async def create_blog(payload: BlogCreate):
    now = datetime.utcnow()
    doc = payload.dict()
    if not doc.get("slug") and doc.get("title"):
        doc["slug"] = slugify(doc["title"])
    doc["created_at"] = now
    doc["updated_at"] = now
    res = await db.blogs.insert_one(doc)
    return {"id": str(res.inserted_id)}

@router.get("/", response_model=List[dict])
async def list_blogs(limit: int = 20):
    out = []
    cursor = db.blogs.find().sort("created_at", -1).limit(limit)
    async for d in cursor:
        d["id"] = str(d["_id"])
        d.pop("_id", None)
        out.append(d)
    return out

@router.get("/{slug}", response_model=dict)
async def get_blog(slug: str):
    doc = await db.blogs.find_one({"slug": slug})
    if not doc:
        raise HTTPException(status_code=404, detail="Blog not found")
    doc["id"] = str(doc["_id"])
    doc.pop("_id", None)
    return doc

@router.put("/{id}", response_model=dict)
async def update_blog(id: str, payload: BlogUpdate):
    update_data = {k: v for k, v in payload.dict().items() if v is not None}
    if update_data:
        update_data["updated_at"] = datetime.utcnow()
        res = await db.blogs.update_one({"_id": ObjectId(id)}, {"$set": update_data})
        if res.matched_count == 0:
            raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}

@router.delete("/{id}", response_model=dict)
async def delete_blog(id: str):
    res = await db.blogs.delete_one({"_id": ObjectId(id)})
    if res.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}
