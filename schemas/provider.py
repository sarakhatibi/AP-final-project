
from sqlmodel import SQLModel, Field
from typing import Optional

class ProviderCreate(SQLModel):
    name: str
    contact: Optional[str] = None
    email: Optional[str] = None
    delivery_time: Optional[int] = None
    active: bool = True

class ProviderRead(SQLModel):
    id: int
    name: str
    contact: Optional[str] = None
    email: Optional[str] = None
    delivery_time: Optional[int] = None
    active: bool

class ProviderUpdate(SQLModel):
    name: Optional[str] = None
    contact: Optional[str] = None
    email: Optional[str] = None
    delivery_time: Optional[int] = None
    active: Optional[bool] = None
    