from fastapi import APIRouter,Depends
from db.database import get_db
from sqlalchemy.orm import Session
from db import Article
from db.schema import ArticleCreate,ArticleDisplay
from typing import List
from db.model import ArticleTable

router = APIRouter(
    prefix='/Article',
    tags=['Article']
)

@router.post('/',response_model=ArticleDisplay)
def Create(request: ArticleCreate, db:Session = Depends(get_db)):
    return Article.CreateArticle(db,request)

@router.get('/{id}')
def getArticle(id: int,db:Session = Depends(get_db)):
    return Article.getArticle(id,db)
