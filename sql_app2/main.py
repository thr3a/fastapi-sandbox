from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine

# データベースを作成
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# response_model
# 400返す

@app.post("/users")
def create_user(user: schemas.User, db: Session = Depends(get_db)):
  new_user = models.User(email=user.email)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
