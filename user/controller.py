from fastapi import Header, HTTPException, Depends
from utils.jwt import decode_token
from db.models import User
from db.session import SessionLocal
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(authorization: str = Header(...), db: Session = Depends(get_db)):
    try:
        token = authorization.split(" ")[1]
        payload = decode_token(token)
        user_id = int(payload["sub"])
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(401, detail="User not found")
        return user
    except:
        raise HTTPException(401, detail="Invalid token")