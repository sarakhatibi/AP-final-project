
from typing import Optional
from sqlmodel import SQLModel, Field
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
    provider_id: Optional[int] = Field(default=None)
    status: OrderStatus = Field(..., title="وضعیت سفارش")
    quantity: int = Field(..., title="تعداد", ge=1)
    name: str = Field(..., title="نام سفارش", min_length=1)
    price: float = Field(..., title="قیمت", gt=0)
    category: Optional[str] = Field(default=None)
    order_date: Optional[datetime] = Field(default=None)
    delivery_date: Optional[datetime] = Field(default=None)
    expected_date: Optional[datetime] = Field(default=None)


class OrderRead(SQLModel):
    id: Optional[int] 
    provider_id: Optional[int] 
    status: OrderStatus 
    quantity:int
    order_date: datetime  
    name: str
    price:float
    category: Optional[str] = None

