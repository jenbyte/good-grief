from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import Base, engine, get_db
from .models import models
from .schemas import schemas

## DEV ENV - REMOVE WHEN DONE MAKING DB
Base.metadata.drop_all(engine)
## TODO: REMOVE WHEN DONE MAKING DB

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# USERS # 

@app.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}", response_model=schemas.UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/", response_model=List[schemas.UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users


# USERS - PARTNERS # 

@app.get("/partners/{partner_id}", response_model=schemas.PartnerWithOffers)
def read_partner(partner_id: int, db: Session = Depends(get_db)):
    db_partner = db.query(models.User).filter(
            models.User.id == partner_id, 
            models.User.user_type == "PARTNER"
        ).first()
    if db_partner is None:
        raise HTTPException(status_code=404, detail="Partner not found")
    return db_partner

@app.get("/partners/", response_model=List[schemas.PartnerWithOffers])
def read_partners(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    partners = (
        db.query(models.User)
        .filter(models.User.user_type == "PARTNER")
        .offset(skip)
        .limit(limit)
        .all()
    )
    return partners


# OFFERS # 

@app.post("/offers/", response_model=schemas.OfferOut)
def create_offer(offer: schemas.OfferCreate, db: Session = Depends(get_db)):
    db_offer = models.Offer(**offer.dict())
    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)
    return db_offer

@app.get("/offers/", response_model=List[schemas.OfferOut])
def read_offers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    offers = db.query(models.Offer).offset(skip).limit(limit).all()
    return offers

@app.get("/offers/{offer_id}", response_model=schemas.OfferOut)
def read_offer(offer_id: int, db: Session = Depends(get_db)):
    db_offer = db.query(models.Offer).filter(models.Offer.id == offer_id).first()
    if db_offer is None:
        raise HTTPException(status_code=404, detail="Offer not found")
    return db_offer


# ARTICLES # 

@app.post("/articles/", response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    db_article = models.Article(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

@app.get("/articles/", response_model=List[schemas.Article])
def read_articles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    articles = db.query(models.Article).offset(skip).limit(limit).all()
    return articles

@app.get("/articles/{article_id}", response_model=schemas.Article)
def read_article(article_id: int, db: Session = Depends(get_db)):
    db_article = db.query(models.Article).filter(models.Article.id == article_id).first()
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article