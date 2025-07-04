from fastapi import APIRouter, Depends
from auth.schema import LoginRequest, TokenResponse
from auth.controller import login, get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login_user(data: LoginRequest, db: Session = Depends(get_db)):
    token = login(data.email, data.password, db)
    return {"access_token": token}
