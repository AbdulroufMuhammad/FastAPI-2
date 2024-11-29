from sqlalchemy.orm.session import Session
from db.model import ArticleTable
from db.schema import ArticleCreate
from fastapi import HTTPException,status
from db.exeception import StoryException

def CreateArticle(db:Session,request:ArticleCreate):
    if request.Content.startswith('once upon a time'):
        raise StoryException('no stories please')
    NewArticle = ArticleTable(
        Title = request.Title,
        Content = request.Content,
        Published = request.Published,
        Creator_id = request.Creator_id
    )
    db.add(NewArticle)
    db.commit()
    db.refresh(NewArticle)
    return NewArticle
def getArticle(id:int, db:Session):
    article = db.query(ArticleTable).filter(ArticleTable.id == id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'user with id {id}not found')
    return article
