# SCHEMAS
# - Input/Output with client

from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import List, Optional

from app.enum import UserType

# Parent/Base
class OfferBase(BaseModel):
    title: str
    partner_id: int
    description: Optional[str] = None
    image_url: Optional[str] = None
    is_active: bool = True
    date_start: date
    date_expires: Optional[date] = None
    usage_limit: Optional[int] = None
    usage_count: int = 0

# Input
class OfferCreate(OfferBase):
    pass

# Ouput
class OfferOut(OfferBase):
    id: int

    class Config:
        orm_mode = True


# Parent/Base
class UserBase(BaseModel):
    name: str
    email: str
    user_type: UserType

# Input
class UserCreate(UserBase):
    pass

# Ouput
class UserOut(UserBase):
    id: int
    offers: List[OfferOut] = []

    class Config:
        orm_mode = True

class UserWithOffers(UserOut):
    offers: List[OfferOut]    


class ArticleBase(BaseModel):
    title: str

class ArticleCreate(ArticleBase):
    pass

class Article(ArticleBase):
    id: int

    class Config:
        orm_mode = True