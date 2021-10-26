# python
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel
from pydantic import Field

# FstApi
from fastapi import FastAPI
from fastapi import Query, Body, Path

app = FastAPI()

# Models
class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"

class Location(BaseModel):
    city: str = Field(
        ...,
        min_length=1,
        max_length=150
        )
    state: str = Field(
        ...,
        min_length=1,
        max_length=150
        )
    country: str = Field(
        ...,
        min_length=1,
        max_length=150
        )

class Person(BaseModel):
    first_name: str = Field(
        ..., 
        min_length=1, 
        max_length=50
        )
    last_name: str = Field(
        ..., 
        min_length=1, 
        max_length=50
        )
    age: int = Field(
        ...,
        gt=0,
        le=115
    )
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=False)

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

# Validaciones: Request Body

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID.",
        gt=0
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results