#add this to main.py above the point where you initialized FastAPI
#import
from fastapi import FastAPI
from app import models
from app.db import engine
from app.db import SessionLocal
from fastapi import Depends
from app import crud

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#create the database tables on app startup or reload
models.Base.metadata.create_all(bind=engine)

@app.post("/create_friend")
def create_friend(first_name:str, last_name:str, age:int, db:Session = Depends(get_db)):
  friend = crud.create_friend(db=db, first_name=first_name, last_name=last_name, age=age)
  ##return object created
  return {"friend": friend}
