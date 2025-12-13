from pydantic import BaseModel


class PostCreat(BaseModel):
    title: str
    content: str


class PostResponse(BaseModel):
    title: str
    content: str