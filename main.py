from fastapi import FastAPI
from auth.router import router as auth_router
from user.router import router as user_router
from db.session import engine
from db.models import Base

import time

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(user_router, prefix="/user", tags=["User"])


@app.get("/")
async def root():
    return {"message": "🚀 PION TECH API is running!"}