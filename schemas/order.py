
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
    name: str = Field(..., min_length=1, description="نام کالا الزامی است")
    price: float = Field(..., gt=0, description="قیمت باید بیشتر از صفر باشد")
    quantity: int = Field(..., gt=0, description="تعداد باید بیشتر از صفر باشد")
    provider_id: int = Field(..., description="شناسه تأمین‌کننده الزامی است")
    status: str = Field(..., description="وضعیت سفارش الزامی است")
    category: Optional[str] = Field(None)  # اختیاریه
    expected_date: datetime = Field(..., description="تاریخ تحویل الزامی است")


class OrderRead(SQLModel):
    id: Optional[int] 
    provider_id: Optional[int] 
    status: OrderStatus 
    quantity:int
    order_date: datetime  
    name: str
    price:float
    category: Optional[str] = None
    expected_date: datetime
