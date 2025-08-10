from fastapi import APIRouter, Depends
from sqlmodel import Session
from database.connection import get_db
from services.reportt import get_top_products

router = APIRouter()

@router.get("/top_products")
def report(session: Session = Depends(get_db)):
    result = get_top_products(session)
    return result