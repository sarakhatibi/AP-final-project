# models.py
from sqlmodel import SQLModel, Field
from typing import Optional
from enum import Enum

class Role(str,Enum):
    admin="admin"
    user="user"

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    email: str
    username: str
    hashed_password: str
    role:Role= Role.user