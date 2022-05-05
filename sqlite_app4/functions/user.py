from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models, schemas

def create(user: schemas.User, db: Session):
  hashedPassword = user.password + 'hogehoge'
  new_user = models.User(email=user.email, password=hashedPassword)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

def get_all(db: Session):
  users = db.query(models.User).all()
  return users

def get(id: int, db: Session):
  user = db.query(models.User).filter(models.User.id == id).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
  return user

def delete(id: int, db: Session):
  user = db.query(models.User).filter(models.User.id == id)
  if not user.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'id={id} is not found')
  user.delete(synchronize_session=False)
  db.commit()
  return {"message": "ok"}

def update(id: int, request: models.User, db: Session):
  user = db.query(models.User).filter(models.User.id == id)
  if not user.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'id={id} is not found')
  user.update(request.dict())
  db.commit()
  return user.first()
