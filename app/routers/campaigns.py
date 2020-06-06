from fastapi import APIRouter, HTTPException, Depends, FastAPI
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import schemas
import models
from actions import campaigns

router = APIRouter()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/campaigns/", tags=["campaigns"], response_model=schemas.Campaign)
async def create_campaign(campaign: schemas.CampaignCreate, db: Session = Depends(get_db)):
    db_campaigns = campaigns.get_campaign_by_recipient(db, recipient=campaign.recipient)
    if db_campaigns:
        raise HTTPException(status_code=400, detail="Recipient already registered")
    return campaigns.create_campaign(db=db, campaign=campaign)

@router.get("/campaigns/", tags=["campaigns"])
async def read_campaigns(skip: int = 0, limit: int = 100, db: Session = Depends(get_db) ):
    db_campaigns = campaigns.get_campaigns(db, skip=skip, limit=limit)
    return db_campaigns

@router.get("/campaigns/{campaign_id}", tags=["campaigns"])
async def read_campaign(campaign_id: int, db: Session = Depends(get_db)):
    db_campaigns = campaigns.get_campaign(db, campaign_id=campaign_id)
    if db_campaigns is None:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return db_campaigns


@router.put("/campaigns/", tags=["campaigns"], response_model=schemas.Campaign)
async def update_campaign(campaign_update: schemas.CampaignUpdate, db: Session = Depends(get_db)):
    db_campaigns = campaigns.get_campaign(db=db, campaign_id=campaign_update.id)
    if db_campaigns is None:
        raise HTTPException(status_code=400, detail="Recipient does not exist")
    return campaigns.update_campaign(db=db, db_campaign=db_campaigns, campaign=campaign_update)
