from src.application import app
# from src.config import DBConfig, Config
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker


# def connectDB():
#     engine = create_engine(Config.POSTGRES_URI)
#     if not engine:
#         print('unable to connect DB')
#     session = sessionmaker(bind=engine)
#     print(session)


def main():
    # connectDB()
    app.run(debug=True, port=5000)


if __name__ == "__main__":
    main()
