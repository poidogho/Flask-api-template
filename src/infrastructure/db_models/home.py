from pydantic import BaseModel, constr
from .user import User
from .home_image import HomeImage
from typing import List


class Home(BaseModel):
    __tablename__ = 'home'
    id: str
    authorId: User
    name: str
    price: int
    address: str
    sqrFtSize: int
    description: str
    approved: bool
    homeImages: List[HomeImage]

    class Config:
        orm_mode = True
