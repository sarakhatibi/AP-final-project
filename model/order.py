# models.py
from sqlmodel import SQLModel, Field
from typing import Optional

class Order(SQLModel, table=True): 
    id: Optional[int] = Field(default=None, primary_key=True) 
    order_type: OrderType  # "purchase" or "sales" 
    provider_id: Optional[int] = Field(default=None, foreign_key="provider.id") 
    customer_name: Optional[str] = None 
    status: str  # Draft, Sent, Received, Closed, Pending, Completed, ... 
    order_date: datetime = Field(default_factory=datetime.utcnow) 
 
class OrderItem(SQLModel, table=True): 
    id: Optional[int] = Field(default=None, primary_key=True) 
    order_id: int = Field(foreign_key="order.id") 
    product_id: int = Field(foreign_key="product.id") 
    quantity: int 
    unit_price: float