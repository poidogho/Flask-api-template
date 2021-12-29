from ...domain import HomeService


class HomeHandler:
    def __init__(self, homeService: HomeService) -> None:
        self.homeService = homeService
        pass
