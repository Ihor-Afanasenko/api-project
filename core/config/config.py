from ..singleton import Singleton


class Config(Singleton):
    def __init__(self):
        self.host = "https://jsonplaceholder.typicode.com"
