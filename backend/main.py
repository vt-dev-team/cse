from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
@app.post("/new/post", response_model =schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post = post)
@app.get("/post/{post_id}", response_model=schemas.Post)
def get_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id = post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@app.get("/posts/", response_model=List[schemas.Post])
def get_posts(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip = skip, limit = limit)
    return posts
