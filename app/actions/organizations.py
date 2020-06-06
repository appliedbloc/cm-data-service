from sqlalchemy.orm import Session
from sqlalchemy import update
from fastapi.encoders import jsonable_encoder

import models, schemas


def get_organization(db: Session, organization_id: int):
    return db.query(models.Organization).filter(models.Organization.id == organization_id).first()


def get_organization_by_email(db: Session, contact_email: str):
    return db.query(models.Organization).filter(models.Organization.contact_email == contact_email).first()


def get_organizations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Organization).offset(skip).limit(limit).all()


def create_organization(db: Session, organization: schemas.OrganizationCreate):
    db_organization = models.Organization(**organization.dict())
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    return db_organization


def update_organization(db: Session, db_organization: models.Organization, organization: schemas.OrganizationUpdate):
    org_in = organization.dict(exclude_unset=True)
    obj_data = jsonable_encoder(db_organization)

    for field in obj_data:
        if field in org_in:
            setattr(db_organization, field, org_in[field])

    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    return db_organization
