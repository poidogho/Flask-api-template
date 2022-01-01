from ..db_models import HomeDataModel


class HomeRepository:
    def getHomes():
        return HomeDataModel.query.all()
