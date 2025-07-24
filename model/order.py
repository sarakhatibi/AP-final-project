# models.py
from enum import Enum
from sqlmodel import SQLModel, Field
from typing import Optional
from database.connection import get_db
from datetime import datetime



class OrderStatus(str, Enum):
    draft = "draft"
    sent = "sent"
    received = "received"
    closed = "closed"


class OrderType(str, Enum):
    purchase = "purchase"
    sales = "sales"

class Order(SQLModel, table=True): 
    id: Optional[int] = Field(default=None, primary_key=True) 
    provider_id: Optional[int] = Field(default=None, foreign_key="provider.id")  
    status: OrderStatus 
    quantity:int
    order_date: datetime = Field(default_factory=datetime.utcnow) 
    name: str
    price:float
    category: Optional[str] = None
    delivery_date: Optional[datetime] = None       # تاریخ واقعی تحویل
    expected_date: Optional[datetime] = None       # تاریخ مورد انتظار برای تحویل
 
class OrderItem(SQLModel, table=True): 
    id: Optional[int] = Field(default=None, primary_key=True) 
    user_id: int = Field(foreign_key="user.id")
    product_id: int = Field(foreign_key="product.id") 
    quantity: int 
    unit_price: float
    status: OrderStatus = Field(default=OrderStatus.draft) 



