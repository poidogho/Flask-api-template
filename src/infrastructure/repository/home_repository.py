from ..db_models import HomeDataModel


class HomeRepository:
    def getHomes(self):
        homes = HomeDataModel.query.filter_by(approved=True)
        return [home.toDomain() for home in homes]
