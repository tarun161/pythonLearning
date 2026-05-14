from typing import Optional

from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

# "This will return item_id in String"
# @app.get("/items/1/{item_id}")
# def get_item(item_id):
#     return {"item_id": item_id}
#
# "This will return item_id in String"
# @app.get("/items/2/{item_id}")
# def get_item(item_id:int):
#     return {"item_id": item_id}


# @app.get("/blogs")
# def blogs(limit: int = 10,sort: Optional[str] = None):
#   if sort=="asc":
#       return {"blogs" : f'{limit} blogs in asc order'}
#   elif sort=="desc":
#       return {"blogs" : f'{limit} blogs in desc order'}
#   else:
#       return {"blogs" : f'{limit} blogs '}


class Blog(BaseModel):
    title: str
    body: str
    created_by: Optional[str]

@app.post("/blog")
def create_blog(blog: Blog):
    return {"title": blog.title, "body": blog.body}

