from pydantic import BaseModel, constr


class User(BaseModel):
    __tablename__ = 'user'
    id: str
    firstname: constr(max_length=20)
    lastname: constr(max_length=20)
    othernames: constr(max_length=20)
    email: str
    password: str
    role: str

    class Config:
        orm_mode = True
