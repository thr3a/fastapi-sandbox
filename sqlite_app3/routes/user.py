from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models, database
router = APIRouter()

@router.post("/users", response_model=schemas.ShowUser, tags=["users"])
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
  hashedPassword = request.password + 'hogehoge'
  new_user = models.User(email=request.email, password=hashedPassword)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

@router.get("/users", response_model=List[schemas.ShowUserWithPosts], tags=["users"])
def all_fetch(db: Session = Depends(database.get_db)):
  users = db.query(models.User).all()
  return users

@router.get('/users/{id}', response_model=schemas.ShowUserWithPosts, tags=["users"])
def show(id: int, db: Session = Depends(database.get_db)):
  user = db.query(models.User).filter(models.User.id == id).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
  return user

@router.delete('/users/{id}', tags=["users"])
def delete(id: int, db: Session = Depends(database.get_db)):
  user = db.query(models.User).filter(models.User.id == id)
  if not user.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'id={id} is not found')
  user.delete(synchronize_session=False)
  db.commit()
  return {"message": "ok"}

@router.put("/users/{id}", response_model=schemas.ShowUserWithPosts, tags=["users"])
def update(id: int, request: schemas.User, db: Session = Depends(database.get_db)):
  user = db.query(models.User).filter(models.User.id == id)
  if not user.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'id={id} is not found')
  user.update(request.dict())
  db.commit()
  return user.first()
