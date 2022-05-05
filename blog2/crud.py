from sqlalchemy.orm import Session

"""
Session manages persistence operations for ORM-mapped objects.
Let's just refer to it as a database session for simplicity
"""

from app.models import Friend


def create_friend(db:Session, first_name, last_name, age):
    """
    function to create a friend model object
    """
    # create friend instance 
    new_friend = Friend(first_name=first_name, last_name=last_name, age=age)
    #place object in the database session
    db.add(new_friend)
    #commit your instance to the database
    db.commit()
    #reefresh the attributes of the given instance
    db.refresh(new_friend)
    return new_friend

def get_friend(db:Session, id:int):
    """
    get the first record with a given id, if no such record exists, will return null
    """
    db_friend = db.query(Friend).filter(Friend.id==id).first()
    return db_friend

def list_friends(db:Session):
    """
    Return a list of all existing Friend records
    """
    all_friends = db.query(Friend).all()
    return all_friends


def update_friend(db:Session, id:int, first_name: str, last_name: str, age:int):
    """
    Update a Friend object's attributes
    """
    db_friend = get_friend(db=db, id=id)
    db_friend.first_name = first_name
    db_friend.last_name = last_name
    db_friend.age = age

    db.commit()
    db.refresh(db_friend) #refresh the attribute of the given instance
    return db_friend

def delete_friend(db:Session, id:int):
    """
    Delete a Friend object
    """
    db_friend = get_friend(db=db, id=id)
    db.delete(db_friend)
    db.commit() #save changes to db

We are done with defining the crud operations. Hurray!🥳

Define endpoints
We are almost done. Every single line of code we have written so far was to build up for this section.

Let's head back over to main.py:
add the following after where you initialized your FastAPI instance
from app.db import SessionLocal
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
Remember
SessionLocal is the connection to our db.
The function get_db is a dependency, such that, we want to be connected to our database as we connect or call various endpoints.

Let us see this in use with our first endpoint. Add this to main.py
"""
So that FastAPI knows that it has to treat a variable as a dependency, we will import Depends
"""
from fastapi import Depends

#import crud to give access to the operations that we defined
from app import crud

#define endpoint
@app.post("/create_friend")
def create_friend(first_name:str, last_name:str, age:int, db:Session = Depends(get_db)):
    friend = crud.create_friend(db=db, first_name=first_name, last_name=last_name, age=age)
##return object created
    return {"friend": friend}
Save main.py and head over to your browser http://127.0.0.1.8000/docs, and refresh the page. You will see that we have something new. Like this:
image

Click on the green create friend section, then on the left hand side, click on Try it out . Fill in the fields and click on the blue Execute button.
Depending on what you have entered, your response should be in this format:
{
    "first_name": "mike",
    "id": 1,
    "age": 21,
    "last_name": "dave"
}
We can see that response is a dictionary.

Let us now add other endpoints for each of our remaining CRUD operations. (Please read the comments in the snippets for easier understanding)
get a Friend object
#get/retrieve friend 
@app.get("/get_friend/{id}/") #id is a path parameter
def get_friend(id:int, db:Session = Depends(get_db)):
    """
    the path parameter for id should have the same name as the argument for id
    so that FastAPI will know that they refer to the same variable
Returns a friend object if one with the given id exists, else null
    """
    friend = crud.get_friend(db=db, id=id)
    return friend
list Friend objects
@app.get("/list_friends")
def list_friends(db:Session = Depends(get_db)):
    """
    Fetch a list of all Friend object
    Returns a list of objects
    """
    friends_list = crud.list_friends(db=db)
    return friends_list
update a Friend object
@app.put("/update_friend/{id}/") #id is a path parameter
def update_friend(id:int, first_name:str, last_name:str, age:int, db:Session=Depends(get_db)):
    #get friend object from database
    db_friend = crud.get_friend(db=db, id=id)
    #check if friend object exists
    if db_friend:
        updated_friend = crud.update_friend(db=db, id=id, first_name=first_name, last_name=last_name, age=age)
        return updated_friend
    else:
        return {"error": f"Friend with id {id} does not exist"}
delete friend object
@app.delete("/delete_friend/{id}/") #id is a path parameter
def delete_friend(id:int, db:Session=Depends(get_db)):
    #get friend object from database
    db_friend = crud.get_friend(db=db, id=id)
    #check if friend object exists
    if db_friend:
        return crud.delete_friend(db=db, id=id)
    else:
        return {"error": f"Friend with id {id} does not exist"}
That's it for now!

Discussion (0)
Subscribe
pic
Add to the discussion
Code of Conduct • Report abuse
Read next
angelanascimento profile image
[Python] Estrutura de Repetição 'for'
Angela Araújo - May 2

harinderseera profile image
AWS Cloudfront Manager Utility - How To Guide For Windows
Harinder Seera 🇭🇲 - May 2

jcarlosvale profile image
Booleanos em Python - #06
Joao Carlos Sousa do Vale - Apr 21

balt1794 profile image
Generate NFT Metadata (JSON) using Python - Much Exclusive Doge Yacht Club Collection - Part IV
balt1794 - Apr 30


JMG
Follow
Full Stack Web Developer.
LOCATION
Nairobi
WORK
Full Stack Developer
JOINED
2019年10月10日
More from JMG
Set up and Load Initial Data in Django
#django #python #webdev #beginners
from sqlalchemy.orm import Session

"""
Session manages persistence operations for ORM-mapped objects.
Let's just refer to it as a database session for simplicity
"""

from app.models import Friend


def create_friend(db:Session, first_name, last_name, age):
    """
    function to create a friend model object
    """
    # create friend instance 
    new_friend = Friend(first_name=first_name, last_name=last_name, age=age)
    #place object in the database session
    db.add(new_friend)
    #commit your instance to the database
    db.commit()
    #reefresh the attributes of the given instance
    db.refresh(new_friend)
    return new_friend

def get_friend(db:Session, id:int):
    """
    get the first record with a given id, if no such record exists, will return null
    """
    db_friend = db.query(Friend).filter(Friend.id==id).first()
    return db_friend

def list_friends(db:Session):
    """
    Return a list of all existing Friend records
    """
    all_friends = db.query(Friend).all()
    return all_friends


def update_friend(db:Session, id:int, first_name: str, last_name: str, age:int):
    """
    Update a Friend object's attributes
    """
    db_friend = get_friend(db=db, id=id)
    db_friend.first_name = first_name
    db_friend.last_name = last_name
    db_friend.age = age

    db.commit()
    db.refresh(db_friend) #refresh the attribute of the given instance
    return db_friend

def delete_friend(db:Session, id:int):
    """
    Delete a Friend object
    """
    db_friend = get_friend(db=db, id=id)
    db.delete(db_friend)
    db.commit() #save changes to db
