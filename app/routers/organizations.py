from fastapi import APIRouter, HTTPException, Depends, FastAPI
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import schemas
import models
from actions import organizations

router = APIRouter()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/organizations/", tags=["organizations"], response_model=schemas.Organization)
async def create_organization(organization: schemas.OrganizationCreate, db: Session = Depends(get_db)):
    db_organizations = organizations.get_organization_by_email(db, contact_email=organization.contact_email)
    if db_organizations:
        raise HTTPException(status_code=400, detail="Email already registered")
    return organizations.create_organization(db=db, organization=organization)


@router.get("/organizations/", tags=["organizations"])
async def read_organizations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db) ):
    db_organizations = organizations.get_organizations(db, skip=skip, limit=limit)
    return db_organizations


@router.get("/organizations/{organization_id}", tags=["organizations"])
async def read_organization(organization_id: int, db: Session = Depends(get_db)):
    db_organizations = organizations.get_organization(db, organization_id=organization_id)
    if db_organizations is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_organizations


@router.put("/organizations/", tags=["organizations"], response_model=schemas.Organization)
async def update_organization(organization_update: schemas.OrganizationUpdate, db: Session = Depends(get_db)):
    db_organization = organizations.get_organization(db=db, organization_id=organization_update.id)
    if db_organization is None:
        raise HTTPException(status_code=400, detail="Recipient does not exist")
    return organizations.update_organization(db=db, db_organization=db_organization, organization=organization_update)
