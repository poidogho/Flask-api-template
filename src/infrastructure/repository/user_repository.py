from ..db_models import UserDataModel


class UserRepository:
    def createUser():
        pass

    def getUser(self, userId: str):
        user = UserDataModel.query.get(userId)
        pass

    def getUsers(self):
        users = UserDataModel.query.all()
        userDomains = [user.to_json() for user in users]
        return userDomains
