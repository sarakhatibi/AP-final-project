from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import EmailStr, constr


class UserCreate(SQLModel):
    full_name: str
    email: EmailStr
    username: str
    password: constr(min_length=8)

class UserLogin(SQLModel):
    username: str
    password: str

class UserRead(SQLModel):
    id: int
    full_name: str
    email: EmailStr
    username: str
    role: str

class UserUpdate(SQLModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[constr(min_length=8)] = None