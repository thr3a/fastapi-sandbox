from typing import List
from pydantic import BaseModel

class User(BaseModel):
  id: int
  email: str
  password: str
  class Config:
    orm_mode = True

class Post(BaseModel):
  title: str
  body: str
  class Config:
    orm_mode = True

class ShowUser(BaseModel):
  id: int
  email: str
  posts: List[Post] = []
  class Config:
    orm_mode = True

class ShowPost(BaseModel):
  title: str
  body: str
  creator: ShowUser

  class Config:
    orm_mode = True
