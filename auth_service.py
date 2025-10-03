# app/services/auth_service.py
from passlib.context import CryptContext
from typing import Dict, Optional

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Fake in-memory "database" for testing
fake_users_db: Dict[str, Dict] = {}

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_user(username: str, password: str) -> Dict:
    hashed_password = hash_password(password)
    fake_users_db[username] = {"username": username, "password": hashed_password}
    return fake_users_db[username]

def authenticate_user(username: str, password: str) -> Optional[Dict]:
    user = fake_users_db.get(username)
    if not user:
        return None
    if not verify_password(password, user["password"]):
        return None
    return user
