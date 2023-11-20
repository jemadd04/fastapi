from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

# Creating the post schema using Pydantic
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts =[{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "here are my favorite foods, including steak", "id": 2}]

@app.get("/") # This is a decorator. Turns the function into a path operation. Get is the HTTP method.
def root(): #'async' is needed if you perform asynchronous tasks, such as making an API call, talking to DB. Otherwise its optional. Root is just the name.
    return {"message": "Welcome to my API"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}
