from sqlmodel import create_engine, Session

DATABASE_URL = "sqlite:///./inventory.db" 
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    return Session(engine)

def get_db():
    db = get_session()
    try:
        yield db
    finally:
        db.close()