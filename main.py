from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from typing import Union
from fastapi.responses import ORJSONResponse

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

origins = [
    "https://c3streamfastapi.herokuapp.com",
    "http://isaiambalam.herokuapp.com/items/",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def main():
    return {"message": "Hello World"}




@app.get("/items/", response_class=ORJSONResponse)
async def read_items():
    return [{"item_id": "Foo"}]
