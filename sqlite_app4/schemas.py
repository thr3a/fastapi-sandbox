from typing import List
from pydantic import BaseModel

class User(BaseModel):
  email: str
  password: str

class Post(BaseModel):
  title: str
  body: str

class CreatePost(BaseModel):
  title: str
  body: str
  user_id: int

class ShowUser(BaseModel):
  id: int
  email: str
  class Config:
    orm_mode = True

class ShowPost(BaseModel):
  id: int
  title: str
  body: str
  class Config:
    orm_mode = True

class ShowUserWithPosts(ShowUser):
  posts: List[ShowPost] = []

class ShowPostWithUser(ShowPost):
  title: str
  body: str
  creator: ShowUser
