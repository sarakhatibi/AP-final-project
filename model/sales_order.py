# models.py
from enum import Enum
from sqlmodel import SQLModel, Field
from typing import Optional
from database.connection import get_db
from datetime import datetime



class OrderStatus(str, Enum):
    draft = "Draft"
    sent = "Sent"
    received = "Received"
    closed = "Closed"


class OrderType(str, Enum):
    purchase = "purchase"
    sales = "sales"
 
class OrderItem(SQLModel, table=True): 
    id: Optional[int] = Field(default=None, primary_key=True) 
    product_id: int = Field(foreign_key="product.id") 
    user_id: int = Field(foreign_key="user.id")

    quantity: int 
    unit_price: float
    status: OrderStatus = Field(default=OrderStatus.draft) 



