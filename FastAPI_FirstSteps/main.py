from math import prod
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


@app.get('/salute/{name}')
def home(name: str) -> dict:
    return {'key': f'Welcome {name.capitalize()}!!!!!'}


@app.get('/square/{num}')
def square(num: int) -> dict:
    return {'result': f'The result is {(num ** 2)}',
            'param': num}


@app.get('/double')
def double(num: int) -> dict:
    return {'result': f'The double of {num} is {num * 2}.'}


@app.get('/rect_area')
def rect_area(width: int, height: int = 1) -> dict:
    return {'result': f'The rectangle area is {height * width}. '}


class Product(BaseModel):
    name: str
    price: float


@app.post('/products')
def products(product: Product):
    return {'message': f'Product {product.name} sucessfully added. Price is ${product.price}.',
            'Params': {'product': product.name,
                       'price': product.price}}
