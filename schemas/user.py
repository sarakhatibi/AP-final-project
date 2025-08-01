
from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import EmailStr
from pydantic import BaseModel

class UserCreate(SQLModel):
    full_name: str
    email: EmailStr=Field(unique=True)
    username: str=Field(unique=True)
    password: Optional[str] = Field(default=None, min_length=8)
    role: Optional[str] = "user"


class UserLogin(SQLModel):
    username: str
    password: str

class UserRead(SQLModel):
    id: int
    full_name: str
    email: EmailStr=Field(unique=True)
    username: str=Field(unique=True)
    role: str

class UserUpdate(BaseModel):
    full_name: Optional[str] = Field(default=None)
    username: Optional[str] = Field(default=None, unique=True)
    email: Optional[EmailStr] = Field(default=None, unique=True)
    password: Optional[str] = Field(default=None, min_length=8)




class UserUpdateResponse(BaseModel):
    msg: str
    user: UserRead



class WalletChargeRequest(BaseModel):
    amount: float

class UserwalletRead(SQLModel):
    id: int
    userwallet: float


   