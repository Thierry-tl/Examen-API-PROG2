from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

app = FastAPI()

#Q1
@app.get("/hello")
def read_hello():
    return JSONResponse({"message": "Hello World"}, status_code=200)

#Q2
@app.get("/welcome")
def read_welcome(request: Request,name: str):
    return JSONResponse({"message": f"Welcome {name}"}, status_code=200)

#Q3
@app.post("/students")
def list():
    class Liste(BaseModel):
        référence: str
        FirstName: str
        LastName: str
        age: int

    events_store: List[Liste] = []
    return JSONResponse({"events": events_store}, status_code=100)

#Q4
@app.get("/students")
def read_student_list():
    return JSONResponse({"events": list()}, status_code=200)

#Q5
@app.put("/students")




