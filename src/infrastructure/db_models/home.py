from pydantic import BaseModel, constr
from sqlalchemy.sql.schema import ForeignKey
from dataclasses import dataclass
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Boolean
from ...application import db


@dataclass
class HomeDataModel(db.Model):
    __tablename__ = 'Home'
    id = Column(String, primary_key=True, nullable=False)
    authorId = Column(String, ForeignKey('User.id'), nullable=False)
    name = Column(nullable=False)
    price = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    sqrFtSize = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    approved = Column(Boolean, nullable=True)

    def __repr__(self) -> str:
        return f'<Home {self.name}>'

    def toDomain(self):
        return{
            'id': self.id.hex,
            'name': self.name,
            'price': self.price,
            'address': self.address,
            'sqrFtSize': self.sqrFtSize,
            'description': self.description
        }
