from dataclasses import dataclass
from sqlalchemy import Column, String
from ...application import db


@dataclass
class UserDataModel(db.Model):
    __tablename__ = 'User'
    id = Column(String, primary_key=True, nullable=False)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    othernames = Column(String(20), nullable=False)
    email = Column(nullable=False, unique=True)
    password = Column(nullable=False)
    role = Column(nullable=False)

    def __init__(self, id, firstname, lastname, othernames, email, password, role):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self) -> str:
        return f'<User {self.email}>'

    def before_save(self, *args, **kwargs):
        print('attemp saving user')

    def after_save(self, *args, **kwargs):
        print('uSER sAVED')

    def save(self, commit=True):
        self.before_save()
        db.session.add(self)
        if commit:
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
        self.after_save()

    def to_json(self):
        return {
            'id': self.id.hex,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'othernames': self.othernames,
            'email': self.email
        }
