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


@app.get('/animals/{animal_id}')
def get_animal(animal_id: int) -> dict:
    for animal in data_base:
        if animal_id == animal.id:
            return animal
    return {'msg': 'Animal not found.'}


@app.post('/add_animal')
def add_animal(animal: Animal) -> dict:
    if data_base:
        animal.id = data_base[-1].id + 1
    else:
        animal.id = 1
    data_base.append(animal)
    return 'Success!'


@app.delete('/animals/{animal_id}')
def remove_animal(animal_id: int) -> dict:
    for index, animal in enumerate(data_base):
        if animal_id == animal.id:
            return {'msg': 'Animal removed.',
                    'animal_removed': data_base.pop(index)}
    return {'msg': 'Animal not found.'}
