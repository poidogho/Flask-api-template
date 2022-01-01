from .db_config import DBConfig, jwtSecret


class Config(object):
    POSTGRES_URI = f'postgresql://{DBConfig.user}:{DBConfig.password}@{DBConfig.hostMaster}:{DBConfig.port}/{DBConfig.name}'
    JWT_TOKEN_LOCATION = ["json"]
    JWT_SECRET = jwtSecret
