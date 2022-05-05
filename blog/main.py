from telnetlib import SE
from turtle import title
from fastapi import Depends, FastAPI
from requests import Session
from db.models import Post, User
from db.database import Base, SessionLocal, engine
from sqlalchemy.orm import session
from pydantic import BaseModel

app = FastAPI()

Base.metadata.create_all(engine)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.post('/blog')
def create(post: Post, db: Session = Depends(get_db)):
  new_blog = Post(title=post.title, body=post.body)
  db.add(new_blog)
  db.commit()
  db.refresh(new_blog)
  return new_blog
