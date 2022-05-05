from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models, database
router = APIRouter()

@router.post("/posts", tags=["posts"])
def create_post(request: schemas.CreatePost, db: Session = Depends(database.get_db)):
  new_post = models.Post(**request.dict())
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return new_post

@router.get("/posts", response_model=List[schemas.ShowPostWithUser], tags=["posts"])
def all_fetch(db: Session = Depends(database.get_db)):
  posts = db.query(models.Post).all()
  return posts

@router.get('/posts/{id}', response_model=schemas.ShowPostWithUser, tags=["posts"])
def show(id: int, db: Session = Depends(database.get_db)):
  post = db.query(models.Post).filter(models.Post.id == id).first()
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
  return post
