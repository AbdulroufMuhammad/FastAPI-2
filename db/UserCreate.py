from sqlalchemy.orm.session import Session
from db.schema import createUser
from db.model import UserTable
from db.hash import Hash
from db.schema import DisplayUser
from fastapi import HTTPException,status

# Create
def CreateUser(db:Session,request:createUser):
    NewUser = UserTable(
        UserName= request.UserName,
        Email= request.Email,
        Password= Hash.bcrypt(request.Password)
    )
    db.add(NewUser)
    db.commit()
    db.refresh(NewUser)
    return NewUser
# f'User with username {NewUser.UserName} created'

# Read
def Read(db:Session):
    return db.query(UserTable).all()
# Read with id
def Read_with_id(id:int,db:Session):
    user =  db.query(UserTable).filter(UserTable.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details =f'user with id {id}not found')
    return user

# update
def Update_Data(db:Session,id:int, request:CreateUser):
    user = db.query(UserTable).filter(UserTable.id == id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details =f'user with id {id}not found')
    user.update({
        UserTable.UserName: request.UserName,
        UserTable.Email: request.Email,
        UserTable.Password: Hash.bcrypt(request.Password)
    })
    db.commit()
    return ' updated'

# Delete
def Delete(id:int, db:Session ):
    user = db.query(UserTable).filter(UserTable.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details =f'user with id {id}not found')
    db.delete(user)
    db.commit()