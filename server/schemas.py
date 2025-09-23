# schemas.py file for Pydantic models with data validation

from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import List, Optional

class TalkBase(BaseModel):
    title: str
    description: str
    start_time: datetime
    end_time: datetime

class TalkCreate(TalkBase):
    speaker_id: int

class Talk(TalkBase):
    id: int
    speaker_id: int

    class Config:
        orm_mode = True

class SpeakerBase(BaseModel):
    name: str
    bio: str
    company: str

class SpeakerCreate(SpeakerBase):
    pass

class Speaker(SpeakerBase):
    id: int
    talks: List[Talk] = []

    class Config:
        orm_mode = True

class SpeakerWithTalks(Speaker):
    talks: List[Talk]

    



class CouponBase(BaseModel):
    name: str
    is_active: bool
    date_start: date | Optional[date] = None # date = Field(default_factory=date.today)
    date_expires: date | Optional[date] = None # NULL = no expiry

class CouponCreate(CouponBase):
    organization_id: int

class Coupon(CouponBase):
    id: int
    organization_id: int

    class Config:
        orm_mode = True


class OrganizationBase(BaseModel):
    name: str

class OrganizationCreate(OrganizationBase):
    pass

class Organization(OrganizationBase):
    id: int
    coupons: List[Coupon] = []

    class Config:
        orm_mode = True

class OrganizationWithCoupons(Organization):
    coupons: List[Coupon]    


class ArticleBase(BaseModel):
    title: str

class ArticleCreate(ArticleBase):
    pass

class Article(ArticleBase):
    id: int

    class Config:
        orm_mode = True