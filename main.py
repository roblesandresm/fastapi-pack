# python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FstApi
from fastapi import FastAPI
from fastapi import Query, Body

app = FastAPI()

# Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = True

@app.get("/")
def home():
    return {"hello": "world"}

@app.get("/users/{id}")
def users(id: int):
    return {
        "id": id,
        "username": "crashzedran",
        "email": "crashzedrandev@gmail.com",
    }

# Request and Response Body
@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person

# Validaciones: Query parameters

@app.get("/person/details")
def show_person(
    name: Optional[str] = Query(None, min_length = 1, max_length = 50),
    age: str = Query(...)
):
    return {name: age}