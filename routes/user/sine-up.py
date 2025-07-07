from fastapi import APIRouter, Depends,HTTPException 
from sqlmodel import Session, select 
from database.connection import get_session 
from schemas.user import UserCreate
from schemas.user import UserLogin
from model.user import User


def get_db(): 
    with get_session() as session: 
        yield session 

router = APIRouter() 
@router.post("/signup")

def signup(user_create: UserCreate, session: Session = Depends(get_db)):

    hashed = hash_password(user_create.password)
    new_user = User(
        full_name=user_create.full_name,
        email=user_create.email,
        username=user_create.username,
        hashed_password=hashed
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"msg": "ثبت‌ نام موفق"}

@router.post("/login")
def login(credentials: UserLogin, session: Session = Depends(get_db)):
    user = session.exec(select(User).where(User.username == credentials.username)).first()
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="نام کاربری یا رمز اشتباه است")
    
    token = create_access_token({"sub": str(user.id), "role": user.role})
    return {"access_token": token, "token_type": "bearer"}