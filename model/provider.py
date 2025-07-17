# models.py
from sqlmodel import SQLModel, Field
from typing import Optional

class Provider(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    contact: Optional[str] = None
    email: Optional[str] = None
    delivery_time: Optional[int] = None
    active: bool = True #vaziyzat tamin konandeh keh ghabel dastres ast ya nist
