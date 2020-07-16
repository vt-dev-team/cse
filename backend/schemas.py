from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str
    tags: str
    toplevel: int
    date: int
    defunct: bool

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    class Config:
        orm_mode = True