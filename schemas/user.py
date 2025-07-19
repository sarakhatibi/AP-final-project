
from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import EmailStr


class UserCreate(SQLModel):
    full_name: str
    email: EmailStr=Field(unique=True)
    username: str=Field(unique=True)
    password: Optional[str] = Field(default=None, min_length=8)

class UserLogin(SQLModel):
    username: str
    password: str

class UserRead(SQLModel):
    id: int
    full_name: str
    email: EmailStr=Field(unique=True)
    username: str=Field(unique=True)
    role: str

class UserUpdate(SQLModel):
    full_name: Optional[str] = Field(default=None)
    username: Optional[str] = Field(default=None, unique=True)
    email: Optional[EmailStr] = Field(default=None, unique=True)
    password: Optional[str] = Field(default=None, min_length=8)



class Userwallet(SQLModel):
    
    id: int 
    userwallet: float = 0.0



   