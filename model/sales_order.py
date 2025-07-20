from sqlmodel import SQLModel, Field
from typing import Optional
from database.connection import get_db
from datetime import datetime
from model.order import OrderStatus


class OrderItem(SQLModel, table=True): 
    sales_id: Optional[int] = Field(default=None, primary_key=True) 
    product_id: int = Field(foreign_key="product.id")
    quantity: int 
    status: OrderStatus 
    unit_proice:float
    order_date: datetime = Field(default_factory=datetime.utcnow) 
    product_name:str