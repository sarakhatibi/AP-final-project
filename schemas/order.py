
from typing import Optional
from sqlmodel import SQLModel
from datetime import datetime
from model.order import OrderStatus


class OrderUpdate(SQLModel):
  
    quantity:Optional[int] = None  
    name: Optional[str] = None
    price:Optional[float] = None 
    category: Optional[str] = None
    status: Optional[OrderStatus] = None
    order_date: Optional[datetime] = None
    provider_id: Optional[int] = None


class OrderCreate(SQLModel):
    quantity:int
    order_date: datetime  
    name: str
    price:float
    category: Optional[str] = None
    status: OrderStatus= OrderStatus.draft 
    provider_id: int

class OrderRead(SQLModel):
    id: Optional[int] 
    provider_id: Optional[int] 
    status: OrderStatus 
    quantity:int
    order_date: datetime  
    name: str
    price:float
    category: Optional[str] = None

