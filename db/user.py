from fastapi import APIRouter,Depends
from db.schema import createUser
from db.database import get_db
from sqlalchemy.orm import Session
from db import UserCreate
from db.schema import DisplayUser
from typing import List
from db.model import UserTable

router = APIRouter(
    prefix='/User',
    tags=['User']
)
# Create
@router.post('/Create',response_model= DisplayUser)
def Create_User(request: createUser, db:Session = Depends(get_db)):
    return UserCreate.CreateUser(db, request)
  
# Read all

@router.get('/Read')
def get_all_data(db: Session = Depends(get_db)):
    return UserCreate.Read(db)

# Read one
@router.get('/read',response_model=DisplayUser)
def GetUser_byId(id: int, db:Session = Depends(get_db)):
    return UserCreate.Read_with_id(id, db)
# update Data

@router.post('/{id}/update')
def UpdateUser(id: int, request: createUser, db:Session = Depends(get_db)):
    return UserCreate.Update_Data(db, id, request)

# Delete

@router.get('{id}/delete')
def Delete(id: int,db:Session = Depends(get_db)):
    return UserCreate.Delete(id,db)
    