import json
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

openapi_schema = get_openapi(
    title="273_Lab1",
    version="1.0.0",
    description="My First API creation",
    routes=app.routes,
)

with open("273Lab1_openapi.json", "w") as file:
    json.dump(openapi_schema, file)
