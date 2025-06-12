# models.py
from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    email: str
    username: str
    hashed_password: str
    role: str = "user"

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    sku: str     
    price: float
    min_threshold: int  #kamtarin meghdar mojaz dar anbar
    category: Optional[str] = None
    image: Optional[str] = None
    quantity: int = 0

class provider(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    contact: Optional[str] = None
    email: Optional[str] = None
    delivery_time: Optional[int] = None
    active: bool = True #vaziyzat tamin konandeh keh ghabel dastres ast ya nist


class order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  
    name: str
    price: float
    quantity: int = 0
    category: Optional[str] = None
    
        
     