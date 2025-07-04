from fastapi import APIRouter, Depends
from user.controller import get_current_user
from db.models import User

router = APIRouter()

@router.get("/me")
def get_profile(user: User = Depends(get_current_user)):
    return {"id": user.id, "email": user.email}