from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
# from uuid import uuid1

app = FastAPI()


class Animal(BaseModel):
    id: Optional[int]
    name: str
    age: int
    sex: str
    color: str


data_base: List[Animal] = list()


@app.get('/animals')
def list_animals():
    return data_base


@app.post('/add_animal')
def add_animal(animal: Animal) -> dict:
    if data_base:
        animal.id = data_base[-1].id + 1
    else:
        animal.id = 1
    data_base.append(animal)
    return 'Success!'
