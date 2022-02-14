from ..singleton import Singleton


class DBConfig(Singleton):
    def __init__(self) -> None:
        self.driver_name = "postgresql+psycopg2"
        self.host = "127.0.0.1"
        self.port = "5432"
        self.database = "test_result"
        self.user = "postgres"
        self.password = "******"
