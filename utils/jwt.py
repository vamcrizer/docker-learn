from jose import jwt, JWTError
from datetime import datetime, timedelta
SECRET_KEY = "BYN"
ALGORITHM = "HS256"

def create_token(user_id: int):
    payload = {
        "sub": str(user_id), # Subject: ID of user
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
