from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import ai, blogs, users  # your existing routers


app = FastAPI()

# --- CORS Setup ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # allow GET, POST, etc.
    allow_headers=["*"],  # allow all headers
)

# Include your routers
app.include_router(ai.router, prefix="/api/ai")
app.include_router(blogs.router, prefix="/api/blogs")
app.include_router(users.router, prefix="/api/users")
