from .database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  body = Column(String)

class Post(Base):
  __table_name__ = "posts"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  body = Column(String)

