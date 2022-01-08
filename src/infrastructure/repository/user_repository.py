from ..db_models import UserDataModel
from werkzeug.security import generate_password_hash
import uuid


class UserRepository:
    def createUser(self, *user):
        firstname = user[0].get('firstname')
        lastname = user[0].get('lastname')
        othernames = user[0].get('othernames')
        email = user[0].get('email')
        password = self._hashPassword(user[0].get('password'))
        role = user[0].get('role')
        newUser = UserDataModel(
            id=uuid.uuid4(),
            firstname=firstname,
            lastname=lastname,
            othernames=othernames,
            email=email,
            password=password,
            role=role
        )
        newUser.save()
        print(newUser)
        return newUser

    def getUser(self, userId: str):
        user = UserDataModel.query.get(userId)
        pass

    def getUsers(self):
        users = UserDataModel.query.all()
        userDomains = [user.to_json() for user in users]
        return userDomains

    def _hashPassword(self, password):
        return generate_password_hash(password)
