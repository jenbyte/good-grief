# MODELS
# - Defines database structures 

from sqlalchemy import Column, BigInteger, Integer, String, Boolean, ForeignKey, DateTime, Date, Enum, func, and_, text
from sqlalchemy.orm import relationship
from database import Base
from enum import Enum as PyEnum

class TimestampMixins:
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )

class UserType(PyEnum):
    ADMIN = "ADMIN"
    PARTNER = "PARTNER"
    CUSTOMER = "CUSTOMER"

user_type_enum = Enum(
    UserType, name="user_type", create_type=False
)

class User(TimestampMixins, Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    user_type = Column(user_type_enum, nullable=False)

    offers = relationship(
        "Offer", 
        primaryjoin=lambda: and_(
            User.id == Offer.partner_id, 
            User.user_type == 'PARTNER'
        ),
        viewonly=True,
        back_populates="partner"
    )


class Offer(TimestampMixins, Base):
    __tablename__ = "offers"

    id = Column(BigInteger, primary_key=True)
    partner_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    image_url = Column(String)

    date_start = Column(Date, nullable=False, server_default=func.current_date())
    date_expires = Column(Date, nullable=True)
    is_active = Column(Boolean, nullable=False, server_default=text("true"), index=True)

    usage_limit = Column(Integer, nullable=True)
    usage_count = Column(Integer, nullable=False, server_default=text("0"),)

    partner = relationship("User", back_populates="offers")


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String)
    image_url = Column(String)
