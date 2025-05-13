from pydantic import BaseModel

class CreateBlog(BaseModel):
    title: str
    content: str
    author_id: int

class UpdateBlog(CreateBlog):
    title: str
    content: str
    author_id: int

class ShowBlog(BaseModel):
    id: int
    title: str
    content: str
    author_id: int

    class Config:
        orm_mode = True