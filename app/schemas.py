from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    id: int

class User(UserBase):
    id: int
    is_active: bool
    organization_id: int
    email: str
    cell: int
    address_line_one: str
    address_line_two: str
    city: str
    state: str
    zipcode: str
    created_date: datetime
    updated_date: datetime
    first_login_date: datetime
    last_login_date: datetime
    last_session_id: int

    class Config:
        orm_mode = True


class OrganizationBase(BaseModel):
    organization_name: str
    first_name: str
    last_name: str
    contact_email: str
    is_active: bool
    contact_phone: int
    address_line_one: str
    address_line_two: str
    city: str
    state: str
    zipcode: str

class OrganizationCreate(OrganizationBase):
    pass

class OrganizationUpdate(OrganizationBase):
    id: int
    organization_name: str = None
    contact_email: str = None
    first_name: str
    last_name: str
    is_active: bool = None
    contact_phone: int = None
    address_line_one: str = None
    address_line_two: str = None
    city: str = None
    state: str = None
    zipcode: str = None

class Organization(OrganizationBase):
    id: int
    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode = True

class CampaignBase(BaseModel):
    recipient: str
    location: str
    item_requested: str
    item_amount: str
    amount_fulfilled: int
    image_link: str

class CampaignCreate(CampaignBase):
    pass

class CampaignUpdate(CampaignBase):
    id: int
    recipient: str = None
    location: str = None
    item_requested: str = None
    item_amount: str = None
    amount_fulfilled: int = None
    image_link: str = None

class Campaign(CampaignBase):
    id: int

    class Config:
        orm_mode = True

class NeedBase(BaseModel):
    need_name: str

class NeedCreate(NeedBase):
    id: int

class Need(NeedBase):
    id: int
    need_name: str
    is_active: bool
    need_admin_organizations: str
    need_admin_users: str
    need_categories: str
    needed_item: str
    desired_amount: int
    created_date: datetime
    updated_date: datetime
    need_start_date: datetime
    need_end_date: datetime

    class Config:
        orm_mode = True


class DonationBase(BaseModel):
    organization: str
    first_name: str
    last_name: str
    phone: int
    address_one: str
    address_two: str
    city: str
    state: str
    zip_code: str
    campaign_id: int
    item: str
    item_quantity: int


class DonationCreate(DonationBase):
    pass


class DonationUpdate(DonationBase):
    id: int
    organization: str = None
    first_name: str = None
    last_name: str = None
    phone: int = None
    address_one: str = None
    address_two: str = None
    city: str = None
    state: str = None
    zip_code: str = None
    campaign_id: int = None
    item: str = None
    item_quantity: int = None


class Donation(DonationBase):
    id: int

    class Config:
        orm_mode = True
