from .db_config import DBConfig


class Config(object):
    POSTGRES_URI = f'postgresql://{DBConfig.user}:{DBConfig.password}@{DBConfig.hostMaster}/{DBConfig.name}'
