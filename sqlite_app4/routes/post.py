from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database
from ..functions import post

router = APIRouter(
  prefix="/posts",
  tags=["posts"]
)

@router.post("/")
def create_post(request: schemas.CreatePost, db: Session = Depends(database.get_db)):
  return post.create(request, db)

@router.get("/", response_model=List[schemas.ShowPostWithUser])
def get_all(db: Session = Depends(database.get_db)):
  return post.get_all(db)

@router.get('/{id}', response_model=schemas.ShowPostWithUser)
def show(id: int, db: Session = Depends(database.get_db)):
  return post.get(id, db)
