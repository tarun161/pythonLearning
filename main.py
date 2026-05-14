from typing import Optional
from fastapi import FastAPI

from pydantic import BaseModel,ConfigDict

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    id : int
    created_by: str
    created_by: Optional[str]

blog = Blog(title='My Blog', body='My Blog',id = '25' ,created_by='Tarun')

blog_dict: dict = blog.model_dump()
print(blog_dict)

class StrictBlog(BaseModel):
    model_config = ConfigDict(strict=True)
    title: str
    body: str
    id : int
    created_by: str
    created_by: Optional[str]
strict_blog = StrictBlog(title='My Blog', body='My Blog',id = 25 ,created_by='Tarun')
print(StrictBlog.validate(strict_blog.model_dump()))
print(strict_blog.model_dump_json())

