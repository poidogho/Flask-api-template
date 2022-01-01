from pydantic import BaseModel, constr
from sqlalchemy.sql.schema import ForeignKey
from dataclasses import dataclass
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Boolean
Base = declarative_base()


@dataclass
class HomeDataModel(Base):
    __tablename__ = 'home'
    id = Column(String, primary_key=True, nullable=False)
    authorId = Column(String, ForeignKey('user.id'), nullable=False)
    name = Column(nullable=False)
    price = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    sqrFtSize = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    approved = Column(Boolean, nullable=True)

    def fromDomain():
        pass

    def toDomain():
        pass


# class Home(BaseModel):
#     __tablename__ = 'home'
#     id: str
#     authorId: User
#     name: str
#     price: int
#     address: str
#     sqrFtSize: int
#     description: str
#     approved: bool
#     homeImages: List[HomeImage]

#     class Config:
#         orm_mode = True
