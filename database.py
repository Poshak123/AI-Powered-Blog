import motor.motor_asyncio
from .config import MONGODB_URI, DATABASE_NAME

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)
db = client[DATABASE_NAME]

# collections: db.users, db.blogs
