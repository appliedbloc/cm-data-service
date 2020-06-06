from fastapi import APIRouter, HTTPException, Depends, FastAPI
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import schemas
import models
from actions import users

router = APIRouter()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", tags=["users"])
async def create_user(user: schemas.User, db: Session = Depends(get_db)):
    db_user = users.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return users.create_user(db=db, user=user)


@router.get("/users/", tags=["users"])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db) ):
    readed_users = users.get_users(db, skip=skip, limit=limit)
    return readed_users


@router.get("/users/{user_id}", tags=["users"])
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = users.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
