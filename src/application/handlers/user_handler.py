from ...domain.services.user_service import UserService


class UserHandler:
    def __init__(self, userService: UserService) -> None:
        self.userService = userService

    def getUsers(self):
        self.userService.getAllUsers()
