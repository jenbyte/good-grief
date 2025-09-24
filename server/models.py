# models.py file for SQLAlchemy models and relationships

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship
from database import Base

class Speaker(Base):
    __tablename__ = "speakers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    bio = Column(String)
    company = Column(String)

    talks = relationship("Talk", back_populates="speaker")

class Talk(Base):
    __tablename__ = "talks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    speaker_id = Column(Integer, ForeignKey("speakers.id"))
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    speaker = relationship("Speaker", back_populates="talks")

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    coupons = relationship("Coupon", back_populates="organization")


class Coupon(Base):
    __tablename__ = "coupons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    is_active = Column(Boolean)
    date_start = Column(Date, nullable=True)
    date_expires = Column(Date, nullable=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"))

    organization = relationship("Organization", back_populates="coupons")


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)