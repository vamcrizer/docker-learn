from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from db.models import User
from db.session import SessionLocal
from utils.jwt import create_token
import hashlib

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def login(email: str, password: str, db: Session):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    user = db.query(User).filter(User.email == email, User.hashed_password == hashed).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    return create_token(user.id)