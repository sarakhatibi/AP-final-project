from typing import Optional
from jose import jwt, JWTError
from datetime import datetime, timedelta

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
def create_access_token(data: dict):
    to_encode = data.copy()
    
    # زمان انقضا بر اساس نقش
    role = data.get("role", "user")
    expire_minutes = 30 if role == "user" else 180  # مثلاً ۳ ساعت برای admin
    
    expire = datetime.utcnow() + timedelta(minutes=expire_minutes)
    to_encode.update({"exp": expire})
    
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)