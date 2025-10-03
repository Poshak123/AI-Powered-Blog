from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
# app/routes/ai.py
from app.services.ai_service import generate_content
from typing import Optional

router = APIRouter()

class PromptIn(BaseModel):
    prompt: str
    max_tokens: Optional[int] = 300

@router.post("/generate")
async def generate_ai_content(payload: PromptIn):
    try:
        text = generate_content(payload.prompt, payload.max_tokens)
        return {"text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
