from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import Session, select
from database.connection import get_session
from model.user import User
from schemas.user import UserRead
from security.auth import get_current_user

router = APIRouter(tags=["Users"])

def get_db():
    with get_session() as session:
        yield session

@router.get("/users", response_model=list[UserRead])
def get_all_users(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    session: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Access denied. Only admins can see all users.")
    offset = (page - 1) * limit
    query = select(User).offset(offset).limit(limit)
    users = session.exec(query).all()
    if not users:
        raise HTTPException(status_code=404, detail="هیچ کاربری در این صفحه پیدا نشد.")
    return users
