from pydantic import BaseModel
from ..users.schemas import UserOut

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    user: UserOut

class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int