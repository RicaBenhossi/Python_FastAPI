from fastapi import FastAPI


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
