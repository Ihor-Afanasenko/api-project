from core import Singleton
from core import Config
from core import Photo
from requests import get, post


class PhotoService(Singleton):
    def __init__(self, config: Config) -> None:
        self.__config = config

    def get_response_status_code(self) -> int:
        return get(url=f"{self.__config.host}/photos").status_code

    def get_photo_by_id(self, photo_id: int) -> Photo:
        return Photo.from_response_json(
            get(url=f"{self.__config.host}/photos/{photo_id}").json()
        )

    def add_new_photo(self, albumId: int, title: str, url: str, thumbnailUrl: str) -> Photo:
        data = {}
        data.setdefault("albumId", albumId)
        data.setdefault("title", title)
        data.setdefault("url", url)
        data.setdefault("thumbnailUrl", thumbnailUrl)
        return Photo.from_response_json(
            post(url=f"{self.__config.host}/photos", data=data).json()
        )
