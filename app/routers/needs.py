from fastapi import APIRouter, HTTPException, Depends, FastAPI
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import schemas
import models
from actions import  needs

router = APIRouter()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/needs/", tags=["needs"])
async def create_need(need: schemas.Need, db: Session = Depends(get_db)):
    db_needs = needs.get_need_by_name(db, need_name=need.need_name)
    if db_needs:
        raise HTTPException(status_code=400, detail="Need already registered")
    return needs.create_need(db=db, need=need)


@router.get("/needs/", tags=["needs"])
async def read_needs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db) ):
    db_needs = needs.get_needs(db, skip=skip, limit=limit)
    return db_needs


@router.get("/needs/{need_id}", tags=["needs"])
async def read_need(need_id: int, db: Session = Depends(get_db)):
    db_needs = needs.get_need(db, need_id=need_id)
    if db_needs is None:
        raise HTTPException(status_code=404, detail="Need not found")
    return db_needs
