from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    name: str
    email: str
    password: str

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config:
        orm_mode = True



#response models
class showUser(User):
    name: str
    email: str
    blogs: List[Blog] = []
    class Config:
        orm_mode = True

class showBlog(BaseModel):  #response model
    title: str
    body: str
    creator: showUser
    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str
    

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
    user_id: Optional[int] = None



