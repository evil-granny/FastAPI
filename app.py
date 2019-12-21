from datetime import datetime
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from starlette.responses import JSONResponse
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()


class RoomOfHotel(BaseModel):
    id: int
    number: int
    price: int
    description: str = None


roomGlobal = [{
    "id": 0,
    "number": 1,
    "price": 200,
    "description": "Suite"
},
    {
        "id": 1,
        "number": 2,
        "price": 1000,
        "description": "Luxury"
    },
    {
        "id": 2,
        "number": 3,
        "price": 500,
        "description": "Suite"
    }]


@app.get("/")
def get():
    return roomGlobal


@app.get("/room/{id}")
def getRoomById(id):
    return roomGlobal[int(id)]

@app.post("/create")
async def create(room: RoomOfHotel):
    jsonData = jsonable_encoder(room)
    roomGlobal.append(jsonData)
    return roomGlobal


@app.delete('/delete/{id}')
def delete(id: str):
    return roomGlobal.pop(int(id))


@app.put('/update/{id}')
def update(room: RoomOfHotel, id: str):
    roomGlobal[int(id)] = jsonable_encoder(room)
    return roomGlobal[int(id)]
