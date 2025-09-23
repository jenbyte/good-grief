from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/speakers/", response_model=schemas.Speaker)
def create_speaker(speaker: schemas.SpeakerCreate, db: Session = Depends(get_db)):
    db_speaker = models.Speaker(**speaker.dict())
    db.add(db_speaker)
    db.commit()
    db.refresh(db_speaker)
    return db_speaker

@app.get("/speakers/", response_model=List[schemas.Speaker])
def read_speakers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    speakers = db.query(models.Speaker).offset(skip).limit(limit).all()
    return speakers

@app.get("/speakers/{speaker_id}", response_model=schemas.SpeakerWithTalks)
def read_speaker(speaker_id: int, db: Session = Depends(get_db)):
    db_speaker = db.query(models.Speaker).filter(models.Speaker.id == speaker_id).first()
    if db_speaker is None:
        raise HTTPException(status_code=404, detail="Speaker not found")
    return db_speaker

@app.post("/talks/", response_model=schemas.Talk)
def create_talk(talk: schemas.TalkCreate, db: Session = Depends(get_db)):
    db_talk = models.Talk(**talk.dict())
    db.add(db_talk)
    db.commit()
    db.refresh(db_talk)
    return db_talk

@app.get("/talks/", response_model=List[schemas.Talk])
def read_talks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    talks = db.query(models.Talk).offset(skip).limit(limit).all()
    return talks

@app.get("/talks/{talk_id}", response_model=schemas.Talk)
def read_talk(talk_id: int, db: Session = Depends(get_db)):
    db_talk = db.query(models.Talk).filter(models.Talk.id == talk_id).first()
    if db_talk is None:
        raise HTTPException(status_code=404, detail="Talk not found")
    return db_talk




@app.post("/organizations/", response_model=schemas.Organization)
def create_organization(organization: schemas.OrganizationCreate, db: Session = Depends(get_db)):
    db_organization = models.Organization(**organization.dict())
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    return db_organization

@app.get("/organizations/", response_model=List[schemas.Organization])
def read_organizations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    organizations = db.query(models.Organization).offset(skip).limit(limit).all()
    return organizations

@app.get("/organizations/{organization_id}", response_model=schemas.OrganizationWithCoupons)
def read_organization(organization_id: int, db: Session = Depends(get_db)):
    db_organization = db.query(models.Organization).filter(models.Organization.id == organization_id).first()
    if db_organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_organization

@app.post("/coupons/", response_model=schemas.Coupon)
def create_coupon(coupon: schemas.CouponCreate, db: Session = Depends(get_db)):
    db_coupon = models.Coupon(**coupon.dict())
    db.add(db_coupon)
    db.commit()
    db.refresh(db_coupon)
    return db_coupon

@app.get("/coupons/", response_model=List[schemas.Coupon])
def read_coupons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    coupons = db.query(models.Coupon).offset(skip).limit(limit).all()
    return coupons

@app.get("/coupons/{coupon_id}", response_model=schemas.Coupon)
def read_coupon(coupon_id: int, db: Session = Depends(get_db)):
    db_coupon = db.query(models.Coupon).filter(models.Coupon.id == coupon_id).first()
    if db_coupon is None:
        raise HTTPException(status_code=404, detail="Coupon not found")
    return db_coupon

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