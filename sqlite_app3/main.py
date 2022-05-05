from typing import List
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

@app.post("/users", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
  hashedPassword = request.password + 'hogehoge'
  new_user = models.User(email=request.email, password=hashedPassword)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

@app.get("/users", response_model=List[schemas.ShowUserWithPosts])
def all_fetch(db: Session = Depends(get_db)):
  users = db.query(models.User).all()
  return users

@app.get('/users/{id}', response_model=schemas.ShowUserWithPosts)
def show(id: int, db: Session = Depends(get_db)):
  user = db.query(models.User).filter(models.User.id == id).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
  return user

@app.delete('/users/{id}')
def delete(id: int, db: Session = Depends(get_db)):
  user = db.query(models.User).filter(models.User.id == id)
  if not user.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'id={id} is not found')
  user.delete(synchronize_session=False)
  db.commit()
  return {"message": "ok"}

@app.put("/users/{id}", response_model=schemas.ShowUserWithPosts)
def update(id: int, request: schemas.User, db: Session = Depends(get_db)):
  user = db.query(models.User).filter(models.User.id == id)
  if not user.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'id={id} is not found')
  user.update(request.dict())
  db.commit()
  return user.first()

@app.post("/posts")
def create_post(request: schemas.CreatePost, db: Session = Depends(get_db)):
  new_post = models.Post(**request.dict())
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return new_post

@app.get("/posts", response_model=List[schemas.ShowPostWithUser])
def all_fetch(db: Session = Depends(get_db)):
  posts = db.query(models.Post).all()
  return posts

@app.get('/posts/{id}', response_model=schemas.ShowPostWithUser)
def show(id: int, db: Session = Depends(get_db)):
  post = db.query(models.Post).filter(models.Post.id == id).first()
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
  return post
