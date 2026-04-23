from FASTAPI import fastAPI

app = FastAPI()

@app.post("/items/")
async def create_item(item: dict):
    return {"item": item}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "item": item}

@app.delete("/item/{item_id}")
async def delete_item(item_id: int):
    return {"item_id": item_id, "message": "Item Deleted"}
