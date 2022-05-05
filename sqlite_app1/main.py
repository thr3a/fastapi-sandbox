from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.post("/users")
def create_user(user: schemas.User, db: Session = Depends(get_db)):
  new_user = models.User(email=user.email)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

@app.get("/users")
def all_fetch(db: Session = Depends(get_db)):
  users = db.query(models.User).all()
  return users

# @app.get('/users/{id}')
# def show(id: int, db: Session = Depends(get_db)):
#   user = db.query(models.User).filter(models.User.id == id).first()
#   return user
@app.get('/users/{id}')
def show(id: int, db: Session = Depends(get_db)):
  user = db.query(models.User).filter(models.User.id == id).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
  return user

# @app.delete('/users/{id}')
# def delete(id: int, db: Session = Depends(get_db)):
#   db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
#   db.commit()
#   return {"message": "ok"}
@app.delete('/users/{id}')
def delete(id: int, db: Session = Depends(get_db)):
  user = db.query(models.User).filter(models.User.id == id)
  if not user.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'id={id} is not found')
  user.delete(synchronize_session=False)
  db.commit()
  return {"message": "ok"}

@app.put("/users/{id}")
def update(id: int, request: schemas.User, db: Session = Depends(get_db)):
  db.query(models.User).filter(models.User.id == id).update(dict(request))
  db.commit()
  return {"message": "ok"}
