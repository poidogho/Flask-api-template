from pydantic import BaseModel


class HomeImage:
    homeId: str
    imageUrl: str

    class Config:
        orm_mode = True
