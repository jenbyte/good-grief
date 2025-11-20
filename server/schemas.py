# SCHEMAS
# - Communicates with client 
# - Setup validation rules

from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import List, Optional

class OfferBase(BaseModel):
    title: str
    description: str
    is_active: bool = True
    date_start: date
    date_expires: Optional[date] = None

# What client sends to create an offer
class OfferCreate(OfferBase):
    partner_id: int

# Return to client
class OfferOut(OfferBase):
    id: int
    partner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    offers: List[OfferOut] = []

    class Config:
        orm_mode = True

class UserWithOffers(User):
    offers: List[OfferOut]    


class ArticleBase(BaseModel):
    title: str

class ArticleCreate(ArticleBase):
    pass

class Article(ArticleBase):
    id: int

    class Config:
        orm_mode = True