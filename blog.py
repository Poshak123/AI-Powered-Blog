from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BlogPost(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    author: str
    created_at: datetime = datetime.utcnow()

    class Config:
        # If using Pydantic V2
        from_attributes = True
