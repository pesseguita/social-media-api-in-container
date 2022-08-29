from datetime import datetime
from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class PostOut(PostBase):
    id: int
    created_at: datetime