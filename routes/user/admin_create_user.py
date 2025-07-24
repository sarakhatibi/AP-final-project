from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from database.connection import get_db
from schemas.user import UserCreate
from model.user import User, Userwallet
from security.hash import hash_password
from security.auth import get_current_user  # تابع گرفتن یوزر لاگین‌شده

router = APIRouter()

@router.post("/admin/create-user", status_code=status.HTTP_201_CREATED)
def create_user_by_admin(
    user_create: UserCreate,
    session: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # 🔐 بررسی اینکه فقط ادمین بتونه کاربر بسازه
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="دسترسی فقط برای ادمین‌ها مجاز است."
        )

    # بررسی اینکه ایمیل یا نام‌کاربری قبلاً ثبت نشده باشه
    statement = select(User).where(
        (User.email == user_create.email) | (User.username == user_create.username)
    )
    existing_user = session.exec(statement).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ایمیل یا نام‌کاربری قبلاً استفاده شده."
        )

    # ساخت یوزر جدید
    hashed = hash_password(user_create.password)
    new_user = User(
        full_name=user_create.full_name,
        email=user_create.email,
        username=user_create.username,
        hashed_password=hashed,
        role=user_create.role  # "user" یا "admin"
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    # ساخت کیف‌پول برای یوزر جدید
    new_wallet = Userwallet(id=new_user.id, userwallet=0.0)
    session.add(new_wallet)
    session.commit()
    session.refresh(new_wallet)

    return {
        "msg": "✅ کاربر با موفقیت ساخته شد.",
        "user_id": new_user.id,
        "role": new_user.role
    }