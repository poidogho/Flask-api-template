from ...infrastructure import UserRepository


class UserService:
    def __init__(self, userRepository: UserRepository) -> None:
        self.userRepository = userRepository

    def getAllUsers(self):
        self.userRepository.getUsers()
