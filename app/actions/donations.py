from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

import models, schemas


def get_donation(db: Session, donation_id: int):
    return db.query(models.Donation).filter(models.Donation.id == donation_id).first()


def get_donation_by_campaign_id(db: Session, campaign_id: int):
    return db.query(models.Donation).filter(models.Donation.campaign_id == campaign_id).first()


def get_donations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Donation).offset(skip).limit(limit).all()


def create_donation(db: Session, donation: schemas.DonationCreate):
    db_donation = models.Donation(**donation.dict())
    db.add(db_donation)
    db.commit()
    db.refresh(db_donation)
    return db_donation


def update_donation(db: Session, db_donation: models.Donation, donation: schemas.DonationUpdate):
    donation_in = donation.dict(exclude_unset=True)
    obj_data = jsonable_encoder(db_donation)

    for field in obj_data:
        if field in donation_in:
            setattr(db_donation, field, donation_in[field])

    db.add(db_donation)
    db.commit()
    db.refresh(db_donation)
    return db_donation