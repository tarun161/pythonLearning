from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

"This will return item_id in String"
@app.get("/items/1/{item_id}")
def get_item(item_id):
    return {"item_id": item_id}

"This will return item_id in String"
@app.get("/items/2/{item_id}")
def get_item(item_id:int):
    return {"item_id": item_id}


