# models.py
from enum import Enum
from sqlmodel import SQLModel, Field
from typing import Optional
from database.connection import get_db
from datetime import datetime



class OrderStatus(str, Enum):
    draft = "Draft"
    sent = "Sent"
    recived = "Recived"
    closed = "Closed"


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
   
 
class OrderItem(SQLModel, table=True): 
    id: Optional[int] = Field(default=None, primary_key=True) 
    order_id: int = Field(foreign_key="order.id") 
    product_id: int = Field(foreign_key="product.id") 
    quantity: int 
    unit_price: float




