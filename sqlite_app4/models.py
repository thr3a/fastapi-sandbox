from sqlalchemy import Column, ForeignKey, Integer, String
from .database import Base
from sqlalchemy.orm import relationship

class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, unique=True, index=True)
  password =Column(String)

  posts = relationship("Post", back_populates="creator")

class Post(Base):
  __tablename__ = "posts"
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  body = Column(String)
  user_id = Column(Integer, ForeignKey("users.id"))

  creator = relationship("User", back_populates="posts")
