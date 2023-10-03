from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry
from typing import List

app = FastAPI()

@strawberry.type
class Item:
    id: strawberry.ID
    name: str

itemList: List[Item] = [];

@strawberry.type
class Query:
    @strawberry.field
    def get_items(self) -> List[Item]:
        return itemList

    @strawberry.field
    def get_item(self, id: strawberry.ID) -> Item:
        for item in itemList:
            if(item.id == id):
                return item
        return None

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_item(self, name: str, id: strawberry.ID) -> Item:
        item = Item(name= name, id= id)
        itemList.append(item)
        return item

    @strawberry.mutation()
    def update_name( self, id: strawberry.ID, name: str) -> Item:
        for i,item in enumerate(itemList):
            if(item.id == id):
                temp = Item(name=name, id= id)
                itemList.insert(i,temp)
                return temp
        return None

    @strawberry.mutation()
    def delete_item(self, id: strawberry.ID) -> bool:
        for i, item in enumerate(itemList):
            if item.id == id:
                itemList.pop(i) 
                return True
        return False


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)

@app.get("/")
async def read_root():
    return {"root"}

app.include_router(graphql_app, prefix="/graphql")