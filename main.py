from fastapi import FastAPI

app = FastAPI()

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