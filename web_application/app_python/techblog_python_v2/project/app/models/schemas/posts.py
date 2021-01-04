from pydantic import BaseModel


class Post(BaseModel):
    title: str
    text: str

    class Config:
        orm_mode = True
