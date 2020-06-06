from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy_utils import aggregated
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

from datetime import datetime


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    organization_name = Column(String, index=True)
    contact_email = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    contact_phone = Column(Integer)
    address_line_one = Column(String)
    address_line_two = Column(String)
    city = Column(String)
    state = Column(String)
    zipcode = Column(String)
    is_active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow)

class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    recipient = Column(String)
    location = Column(String)
    item_requested = Column(String)
    item_amount = Column(String)
    @aggregated('donation_totals', Column(Integer))
    def amount_fulfilled(self):
        return func.sum(Donation.item_quantity)

    donation_totals = relationship('Donation')
    image_link = Column(String)

    donations = relationship("Donation", back_populates="campaigns")

class Need(Base):
    __tablename__ = "needs"

    id = Column(Integer, primary_key=True, index=True)
    need_name = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    need_admin_organizations = Column(String)
    need_admin_users = Column(String)
    need_categories = Column(String)
    needed_item = Column(String)
    desired_amount = Column(Integer)
    created_date = Column(DateTime)
    updated_date = Column(DateTime)
    need_start_date = Column(DateTime)
    need_end_date = Column(DateTime)


class Donation(Base):
    __tablename__ = "donations"

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"))
    organization = Column(String)
    item = Column(String)
    item_quantity = Column(Integer)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(Integer)
    address_one = Column(String)
    address_two = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(Integer)

    campaigns = relationship("Campaign", back_populates="donations")

