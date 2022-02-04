from core import Config
from core import Singleton
from core import PostMessage, Comment
from requests import get, post, put, patch, delete


class PostsService(Singleton):
    def __init__(self, config: Config) -> None:
        self.__config = config

    def get_response_status_code(self) -> int:
        return get(url=f"{self.__config.host}/posts").status_code

    def get_post_message_by_id(self, post_id: int) -> PostMessage:
        return PostMessage.from_response_json(
            get(url=f"{self.__config.host}/posts/{post_id}").json()
        )

    def get_post_message_comment_by_ids(self, post_id: int, comment_id: int) -> Comment:
        return Comment.from_response_json(
            (get(url=f"{self.__config.host}/posts/{post_id}/comments")).json()[comment_id - 1]
        )

    def add_new_post_message(self, title: str, body: str, userId: int) -> PostMessage:
        data = {}
        data.setdefault("title", title)
        data.setdefault("body", body)
        data.setdefault("userId", userId)
        return PostMessage.from_response_json(
            post(url=f"{self.__config.host}/posts", data=data).json()
        )

    def update_post_message(self, id: int, title: str, body: str, userId: int) -> PostMessage:
        data = {}
        data.setdefault("id", id)
        data.setdefault("title", title)
        data.setdefault("body", body)
        data.setdefault("userId", userId)
        return PostMessage.from_response_json(
            put(url=f"{self.__config.host}/posts/{id}", data=data).json()
        )

    def patch_post_message(self, id: int, title: str, body: str) -> PostMessage:
        data = {}
        data.setdefault("id", id)
        data.setdefault("title", title)
        data.setdefault("body", body)
        return PostMessage.from_response_json(
            patch(url=f"{self.__config.host}/posts/{id}", data=data).json()
        )

    def delete_post_message_status_code(self, id: int) -> int:
        return delete(url=f"{self.__config.host}/posts/{id}").status_code
