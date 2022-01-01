from dotenv import load_dotenv
import os

load_dotenv()

jwtSecret = os.getenv('JWTSECRET')


class DBConfig(object):
    name = os.getenv('POSTGRES_DATABASE')
    port = os.getenv('POSTGRES_PORT')
    user = os.getenv('POSTGRES_USER')
    hostMaster = os.getenv('POSTGRES_HOST')
    password = os.getenv('POSTGRES_PASSWORD')
    minConnections = os.getenv('POSTGRES_MIN_CONNS')
    maxConnections = os.getenv('POSTGRES_MAX_CONNS')
