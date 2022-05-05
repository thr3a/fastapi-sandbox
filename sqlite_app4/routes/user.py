from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database
from ..functions import user

router = APIRouter(
  prefix="/users",
  tags=["users"]
)

@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
  return user.create(request, db)

@router.get("/", response_model=List[schemas.ShowUserWithPosts])
def get_all(db: Session = Depends(database.get_db)):
  return user.get_all(db)

@router.get('/{id}', response_model=schemas.ShowUserWithPosts)
def show(id: int, db: Session = Depends(database.get_db)):
  return user.get(id, db)

@router.delete('/{id}')
def delete(id: int, db: Session = Depends(database.get_db)):
  return user.delete(id, db)

@router.put("/{id}", response_model=schemas.ShowUser)
def update(id: int, request: schemas.User, db: Session = Depends(database.get_db)):
  return user.update(id, request, db)
