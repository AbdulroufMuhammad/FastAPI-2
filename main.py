from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from db import model
from db.database import engine
from db import user
from db import CreateArticle
from db.exeception import StoryException
from fastapi.responses import JSONResponse
from db import product

app = FastAPI()

app.include_router(user.router)
app.include_router(product.router)
app.include_router(CreateArticle.router)


# Exception
@app.exception_handler(StoryException)
def StoryException_err(request:Request,exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={'detail': exc.name}
    )
@app.get('/')
def Home():
    return{'message':'Home'} 


model.Base.metadata.create_all(engine)

origin = ['http://localhost:5173']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origin,
    allow_credentials=True,
    # allow_methods = ["*"],
    # allow_Headers = ["*"],
)