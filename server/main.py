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




@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

@app.get("/users/{user_id}", response_model=schemas.UserWithOffers)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/offers/", response_model=schemas.Offer)
def create_offer(offer: schemas.OfferCreate, db: Session = Depends(get_db)):
    db_offer = models.Offer(**offer.dict())
    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)
    return db_offer

@app.get("/offers/", response_model=List[schemas.Offer])
def read_offers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    offers = db.query(models.Offer).offset(skip).limit(limit).all()
    return offers

@app.get("/offers/{offer_id}", response_model=schemas.Offer)
def read_offer(offer_id: int, db: Session = Depends(get_db)):
    db_offer = db.query(models.Offer).filter(models.Offer.id == offer_id).first()
    if db_offer is None:
        raise HTTPException(status_code=404, detail="Offer not found")
    return db_offer

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