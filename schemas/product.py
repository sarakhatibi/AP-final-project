from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import BaseModel




class ProductCreate(SQLModel):
    name: str
    sku: str
    price: float
    min_threshold: int
    category: Optional[str] = None
    image: Optional[str] = None
    quantity: int = 0

class ProductRead(SQLModel):
    id: int
    name: str
    sku: str
    price: float
    min_threshold: int
    category: Optional[str] = None
    image: Optional[str] = None
    quantity: int

class ProductUpdate(SQLModel):
    name: Optional[str] = None
    sku: Optional[str] = None
    price: Optional[float] = None
    min_threshold: Optional[int] = None
    category: Optional[str] = None
    image: Optional[str] = None
    quantity: Optional[int] = None

class LowStockAlert(BaseModel):
    name: str
    sku: str
    quantity: int
    min_threshold: int
    alert: str

