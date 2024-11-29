from fastapi import APIRouter,Response,Form

router = APIRouter(
    prefix= '/Product',
    tags=['product']
)


product = ['spoon','rice','plate']

@router.get('/all')
def Product():
    data = " ".join(product)
    return Response(content=data,media_type="text/plain")

@router.post('/')
def createProduct (name:str = Form(...)):
    product.append(name)
    return product
