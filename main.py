# python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FstApi
from fastapi import FastAPI
from fastapi import Query, Body, Path

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
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50,
        title="Person Name",
        description="this is the person name. It's between 1 and 50 characters"
    ),
    age: str = Query(
        ...,
        title="Person age",
        description="this is the person age. It's required"
    )
):
    return {name: age}

# Validations path parameters
@app.get("/person/details/{person_id}")
def show_person(
    person_id: int = Path(
        ..., gt=0,
        title = "Person Id",
        description = "This is the person Id. It's required"
    )
):
    return {person_id: "It exists!"}