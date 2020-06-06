from sqlalchemy.orm import Session

import models, schemas


def get_need(db: Session, need_id: int):
    return db.query(models.Need).filter(models.Need.id == need_id).first()


def get_need_by_name(db: Session, need_name: str):
    return db.query(models.Need).filter(models.Need.need_name == need_name).first()


def get_needs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Need).offset(skip).limit(limit).all()


def create_need(db: Session, need: schemas.Need):
    db_need = models.Need(need_name=need.need_name)
    db.add(db_need)
    db.commit()
    db.refresh(db_need)
    return db_need
