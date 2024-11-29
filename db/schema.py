from pydantic import BaseModel
from typing import List

class Article(BaseModel):
    title: str
    content: str
    published: bool
    class Config:
      orm_mode = True

class createUser(BaseModel):
    UserName: str
    Email: str
    Password: str

class DisplayUser(BaseModel):
    UserName: str
    Email: str
    items: List[Article] = []
    class Config:
      orm_mode = True

# Convert `UserR` into a Pydantic model
class UserR(BaseModel):
    id: int
    UserName: str
    class Config:
      orm_mode = True

class ArticleCreate(BaseModel):
    Title: str
    Content: str
    Published: bool
    Creator_id: int

class ArticleDisplay(BaseModel):
    Title: str
    Content: str
    Published: bool
    User: UserR  
    class Config:
      orm_mode = True
