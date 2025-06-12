# models.py
from sqlmodel import SQLModel, Field
from typing import Optional

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    sku: str     
    price: float
    min_threshold: int  #kamtarin meghdar mojaz dar anbar
    category: Optional[str] = None
    image: Optional[str] = None
    quantity: int = 0