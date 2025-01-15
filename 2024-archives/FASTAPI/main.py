from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    print(item_id)
    return {"item_id": item_id}

@app.get("/items")
async def read_item(item_id: int):
    return {"item_id": item_id}

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.post("/items/")
async def create_item(item: Item):
    return item
