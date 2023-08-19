from fastapi import FastAPI, Body, Depends
import schemas
import models

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


app = FastAPI()




@app.get("/")
def getUser(session: Session = Depends(get_session)):
    users = session.query(models.User).all()
    return users


@app.get("/{id}")
def getUser(id:int, session: Session = Depends(get_session)):
    user = session.query(models.User).get(id)
    return user

# @app.post('/')
# def addItem(task:str):
#     newId = len(fakeDatabase.keys()) +1
#     fakeDatabase[newId] = {"task": task}
#     return fakeDatabase


@app.post('/')
def addUser(request: schemas.User, session: Session = Depends(get_session)):
    user = models.User(users=request.user)
    session.add(user)
    session.commit()
    session.refresh(user)

    return user

# @app.post("/")
# def addItem(item:schemas.Item, session = Depends(get_session)):
#     item = models.Item(task = item.task)
#     session.add(item)
#     session.commit()
#     session.refresh(item)
#     return item

@app.put('/{id}')
def updateUser(id:int, user:schemas.User, session: Session = Depends(get_session) ):
   userObject = session.query(models.User).get(id)
   userObject.users = user.user
   session.commit()
   return userObject


@app.delete('/{id}')
def deleteUser(id:int, session = Depends(get_session)):
    user_object = session.query(models.User).filter_by(id= id).first()
    if user_object:
        session.delete(user_object)
        session.commit()
        session.close()
    return "item was delete..."


# item_object = session.query(Item).filter_by(id=item_id).first()
# if item_object:
#     session.delete(item_object)
#     session.commit()





