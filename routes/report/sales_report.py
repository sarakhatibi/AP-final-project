from fastapi import APIRouter, Depends
from datetime import datetime
from sqlmodel import Session
from database.connection import get_db 
from services.reportt import get_top_products

router = APIRouter()

@router.get("/top-products")
def report(from_date: str, to_date: str, session=Depends(get_db)):
    start = datetime.fromisoformat(from_date)
    end = datetime.fromisoformat(to_date)
    result = get_top_products(start, end, session)
    return result