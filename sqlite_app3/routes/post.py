from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models, database
router = APIRouter()

@router.get('/posts/{id}', response_model=schemas.ShowPostWithUser, tags=["posts"])
def show(id: int, db: Session = Depends(database.get_db)):
  post = db.query(models.Post).filter(models.Post.id == id).first()
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
  return post
