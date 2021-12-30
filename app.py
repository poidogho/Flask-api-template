from src.application import app
from src.config import DBConfig, Config
from sqlalchemy import create_engine


def connectDB():
    engine = create_engine(Config.POSTGRES_URI)
    if not engine:
        print('unable to connect DB')


def main():
    connectDB()
    app.run(debug=True, port=5000)


if __name__ == "__main__":
    main()
