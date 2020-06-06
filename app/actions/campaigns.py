from sqlalchemy.orm import Session
from sqlalchemy import update
from fastapi.encoders import jsonable_encoder

import models, schemas


def get_campaign(db: Session, campaign_id: int):
    return db.query(models.Campaign).filter(models.Campaign.id == campaign_id).first()


def get_campaign_by_recipient(db: Session, recipient: str):
    return db.query(models.Campaign).filter(models.Campaign.recipient == recipient).first()


def get_campaigns(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Campaign).offset(skip).limit(limit).all()


def create_campaign(db: Session, campaign: schemas.CampaignCreate):
    db_campaign = models.Campaign(**campaign.dict())
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)
    return db_campaign


def update_campaign(db: Session, db_campaign: models.Campaign, campaign: schemas.CampaignUpdate):
    campaign_in = campaign.dict(exclude_unset=True)
    obj_data = jsonable_encoder(db_campaign)

    for field in obj_data:
        if field in campaign_in:
            setattr(db_campaign, field, campaign_in[field])

    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)
    return db_campaign
