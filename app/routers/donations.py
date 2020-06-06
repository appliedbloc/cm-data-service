from fastapi import APIRouter, HTTPException, Depends, FastAPI
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import schemas
import models
from actions import donations

router = APIRouter()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/donations/", tags=["donations"], response_model=schemas.Donation)
async def create_donation(donation: schemas.DonationCreate, db: Session = Depends(get_db)):
    # TODO: HANDLE DUPES
    # db_donations = donations.get_donation_by_campaign_id(db, campaign_id=donation.campaign_id)
    # if db_donations:
    #     raise HTTPException(status_code=400, detail="Recipient already registered")
    return donations.create_donation(db=db, donation=donation)

@router.get("/donations/", tags=["donations"])
async def read_donations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db) ):
    db_donations = donations.get_donations(db, skip=skip, limit=limit)
    return db_donations

@router.get("/donations/{donation_id}", tags=["donations"])
async def read_donation(donation_id: int, db: Session = Depends(get_db)):
    db_donations = donations.get_donation(db, donation_id=donation_id)
    if db_donations is None:
        raise HTTPException(status_code=404, detail="Donation not found")
    return db_donations

@router.get("/donations/by_campaign_id/{campaign_id}", tags=["donations"])
async def read_donation(campaign_id: int, db: Session = Depends(get_db)):
    db_donations = donations.get_donation_by_campaign_id(db, campaign_id=campaign_id)
    if db_donations is None:
        raise HTTPException(status_code=404, detail="Donation not found")
    return db_donations


@router.put("/donations/", tags=["donations"], response_model=schemas.Donation)
async def update_donation(donation_update: schemas.DonationUpdate, db: Session = Depends(get_db)):
    db_donations = donations.get_donation(db=db, donation_id=donation_update.id)
    if db_donations is None:
        raise HTTPException(status_code=400, detail="Recipient does not exist")
    return donations.update_donation(db=db, db_donation=db_donations, donation=donation_update)
