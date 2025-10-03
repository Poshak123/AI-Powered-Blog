from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserModel(BaseModel):
    id: Optional[str] = Field(alias="_id")
    email: EmailStr
    password: str   # hashed in DB
    name: Optional[str]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
