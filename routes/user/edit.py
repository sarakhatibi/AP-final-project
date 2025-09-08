
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database.connection import get_db
from model.user import User
from schemas.user import UserUpdate, UserRead, UserUpdateResponse
from security.auth import get_current_user
from security.hash import hash_password

router = APIRouter()

# دریافت اطلاعات کاربر
@router.get("/edit", response_model=UserRead)
def get_current_user_info(
    session: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = session.get(User, current_user.id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# ویرایش اطلاعات کاربر
@router.put("/edit", response_model=UserUpdateResponse)
def update_current_user(
    user_update: UserUpdate,
    session: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = session.get(User, current_user.id)
    if not user:
      raise HTTPException(status_code=404, detail="User not found")

    if user_update.full_name is not None:
        user.full_name = user_update.full_name
    if user_update.email is not None:
        user.email = user_update.email
    if user_update.username is not None:
        user.username = user_update.username
    if user_update.password is not None and user_update.password.strip() != "":
        user.hashed_password = hash_password(user_update.password)

    session.add(user)
    session.commit()
    session.refresh(user)

    return {"msg": "اطلاعات شما با موفقیت ویرایش شد", "user": user}