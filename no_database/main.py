from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

userdb = []

class User(BaseModel):
    id: int
    email: str

@app.get("/")
def index():
  return {"hello": "world"}

@app.get("/users")
def get_users():
  return userdb

@app.post("/user")
def add_user(user: User):
  userdb.append(user.dict())
  return userdb[-1]

@app.get("/user/{user_id}")
def get_user(user_id: int):
    user = user_id - 1
    return userdb[user]

@app.post("/users/{user_id}")
def update_user(user_id: int, user: User):
    userdb[user_id] = user
    return {"message": "user has been updated succesfully"}

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    userdb.pop(user_id-1)
    return {"message": "user has been deleted succesfully"}
