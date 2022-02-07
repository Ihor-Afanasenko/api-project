from core import Singleton
from core import Config
from core import Photo
from requests import get, post, put, patch, delete


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

    def updating_photo(self, albumId: int, id: int, title: str, url: str, thumbnailUrl: str) -> Photo:
        data = {}
        data.setdefault("albumId", albumId)
        data.setdefault("id", id)
        data.setdefault("title", title)
        data.setdefault("url", url)
        data.setdefault("thumbnailUrl", thumbnailUrl)
        return Photo.from_response_json(
            put(url=f"{self.__config.host}/photos/{id}", data=data).json()
        )

    def patch_photo(self, albumId, id: int, title: str, url: str) -> Photo:
        data = {}
        data.setdefault("albumId", albumId)
        data.setdefault("id", id)
        data.setdefault("title", title)
        data.setdefault("url", url)
        return Photo.from_response_json(
            patch(url=f"{self.__config.host}/photos/{id}", data=data).json()
        )

    def delete_photo_status_code(self, id: int) -> int:
        return delete(url=f"{self.__config.host}/photos/{id}").status_code
