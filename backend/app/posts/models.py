from pydantic import BaseModel
from ..users.models import UserOut

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    user: UserOut
