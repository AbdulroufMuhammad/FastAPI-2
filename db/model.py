from db.database import Base
from sqlalchemy import Column,String,Integer,Boolean,ForeignKey
from sqlalchemy.orm import relationship

class UserTable(Base):
    __tablename__ = 'Users'

    id = Column(Integer,primary_key=True,index=True )
    UserName = Column(String)
    Email = Column(String)
    Password = Column(String)
    items = relationship("ArticleTable",back_populates='User')

class ArticleTable(Base):
    __tablename__ = 'Article'

    id = Column(Integer,primary_key=True)
    Title = Column(String)
    Content = Column(String)
    Published = Column(Boolean)
    Creator_id = Column(Integer,ForeignKey('Users.id'))
    User = relationship("UserTable",back_populates='items')