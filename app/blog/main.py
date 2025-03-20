from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'abc'}}

@app.get('/blog')
def blogs(limit = 50, published: bool = True, sort: Optional[str] =None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
     return {'data': f'Blog is created with title: {request.title}'}




