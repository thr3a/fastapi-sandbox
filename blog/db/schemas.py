from mimetypes import init
from pydantic import BaseModel

class UserBase(BaseModel):
  id: int
  name: str
  email: str

class PostBase(BaseModel):
  id: int
  title: str
  body: str
