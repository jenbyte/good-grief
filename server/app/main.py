from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import or_
from datetime import date
from typing import List

from app.database import Base, engine, get_db, SessionLocal
from .models import models
from .schemas import schemas
from app.db.mock import mock_data

## DEV ENV - REMOVE WHEN DONE MAKING DB
Base.metadata.drop_all(engine) # only in dev
## TODO: REMOVE WHEN DONE MAKING DB

# Create tables
Base.metadata.create_all(bind=engine)

session = SessionLocal()
mock_data(session) # mock data

app = FastAPI()

# CORS middleware to connect to frontend
origins = [
    "http://localhost:5173",  # React dev
    # TODO: add deployed frontend URL later
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# USERS # 

@app.post("/users", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    print('***CREATE USER: ', db_user)
    return db_user

@app.get("/users", response_model=List[schemas.UserOut])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    print('***CREATE USERS: ', users)
    return users

@app.get("/users/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    print('***GET USER: ', db_user)
    return db_user


# USERS - PARTNERS # 

@app.get("/partners", response_model=List[schemas.PartnerWithOffers])
def get_partners(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    partners = (
        db.query(models.User)
        .filter(models.User.user_type == "PARTNER")
        .offset(skip)
        .limit(limit)
        .all()
    )
    print('***GET PARTNERS: ', partners)
    return partners

@app.get("/partners/{partner_id}", response_model=schemas.PartnerWithOffers)
def get_partner(partner_id: int, db: Session = Depends(get_db)):
    db_partner = db.query(models.User).filter(
            models.User.id == partner_id, 
            models.User.user_type == "PARTNER"
        ).first()
    if db_partner is None:
        raise HTTPException(status_code=404, detail="Partner not found")
    
    print('***GET PARTNER: ', db_partner)
    return db_partner


# OFFERS # 

@app.post("/offers", response_model=schemas.OfferOut)
def create_offer(offer: schemas.OfferCreate, db: Session = Depends(get_db)):
    #Check if user is a partner
    partner = db.query(models.User).filter(
            models.User.id == offer.partner_id, 
            models.User.user_type == "PARTNER"
        ).first()
    if not partner:
        raise HTTPException(status_code=404, detail="Error in user creating new offer")
    if partner.user_type != "PARTNER":
        raise HTTPException(status_code=404, detail="User must be a 'Partner' to create an offer")
    
    new_offer = models.Offer(**offer.dict())
    db.add(new_offer)
    db.commit()
    db.refresh(new_offer)
    return new_offer

# @app.get("/offers", response_model=List[schemas.OfferOut])
# def get_offers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     offers = db.query(models.Offer).offset(skip).limit(limit).all()
#     return offers

@app.get("/offers", response_model=List[schemas.OfferOut])
def get_active_offers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    offers = db.query(models.Offer).filter(
            models.Offer.is_active == True,
            or_(
                models.Offer.date_expires == None,
                models.Offer.date_expires > date.today()
            )
        ).offset(skip).limit(limit).all()
    return offers

@app.get("/offers/{offer_id}", response_model=schemas.OfferOut)
def get_offer(offer_id: int, db: Session = Depends(get_db)):
    db_offer = db.query(models.Offer).filter(models.Offer.id == offer_id).first()
    if db_offer is None:
        raise HTTPException(status_code=404, detail="Offer not found")
    return db_offer


# ARTICLES # 

@app.post("/articles", response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    db_article = models.Article(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

@app.get("/articles", response_model=List[schemas.Article])
def get_articles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    articles = db.query(models.Article).offset(skip).limit(limit).all()
    return articles

@app.get("/articles/{article_id}", response_model=schemas.Article)
def get_article(article_id: int, db: Session = Depends(get_db)):
    db_article = db.query(models.Article).filter(models.Article.id == article_id).first()
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article