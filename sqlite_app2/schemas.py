from pydantic import BaseModel

class User(BaseModel):
  id: int
  email: str
  password: str
  class Config:
    orm_mode = True

class UpdateUser(BaseModel):
  email: str
  password: str
  class Config:
    orm_mode = True


class ShowUser(BaseModel):
  id: int
  email: str

  # NOTE: これしないとvalue is not a valid dict (type=type_error.dict)になる
  class Config:
    orm_mode = True

