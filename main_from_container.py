from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from auth.router import router as auth_router
from user.router import router as user_router
from db.session import engine
from db.models import Base
import os

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DOCKER API",
    description="FastAPI with JWT Authentication + Test Interface",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(user_router, prefix="/users", tags=["User"])

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {
        "message": "🚀 IEC API is running!",
        "version": "1.0.0",
        "test_interface": "/static/index.html",
        "docs": "/docs"
    }