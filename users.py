from fastapi import APIRouter, HTTPException, Depends, Header
from app.database import db
from app.schemas.user import UserCreate, Token
from app.utils.security import hash_password, verify_password, create_access_token, decode_access_token
from bson import ObjectId

router = APIRouter()

@router.post("/register", response_model=dict)
async def register(user: UserCreate):
    existing = await db.users.find_one({"email": user.email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    doc = user.dict()
    doc["password"] = hash_password(doc["password"])
    res = await db.users.insert_one(doc)
    return {"id": str(res.inserted_id)}

@router.post("/login", response_model=Token)
async def login(payload: UserCreate):
    # For simplicity: we expect email and password in the same schema
    user = await db.users.find_one({"email": payload.email})
    if not user or not verify_password(payload.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(subject=str(user["_id"]))
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
async def me(authorization: str = Header(None)):
    """
    Pass header: Authorization: Bearer <token>
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing token")
    try:
        scheme, token = authorization.split()
        payload = decode_access_token(token)
        if not payload:
            raise HTTPException(status_code=401, detail="Invalid token")
        user_id = payload.get("sub")
        user = await db.users.find_one({"_id": ObjectId(user_id)})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user["id"] = str(user["_id"])
        user.pop("_id", None)
        user.pop("password", None)
        return user
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid auth header")
