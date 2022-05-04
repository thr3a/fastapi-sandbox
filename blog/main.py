from fastapi import FastAPI
from .schemas import Blog
from .models import Base
from . import models
from .database import engine, sessionLocal
from sqlalchemy.orm import session


from pydantic import BaseModel
# from .schemas import Blog
from .models import Blog
from .database import Base, engine

app = FastAPI()

Base.metadata.create_all(engine)

@app.post('/blog')
def create(blog: Blog):
  return { 'data': Blog }
