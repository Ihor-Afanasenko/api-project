from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from core.config.db_config import DBConfig
from core import Singleton


class BaseRepository(Singleton):
    def __init__(self) -> None:
        self.__config = DBConfig()
        self.__engine = create_engine(
            f"{self.__config.driver_name}://"
            f"{self.__config.user}:"
            f"{self.__config.password}@"
            f"{self.__config.host}:"
            f"{self.__config.port}/"
            f"{self.__config.database}"
        )
        self._session: Session = sessionmaker(self.__engine)()
