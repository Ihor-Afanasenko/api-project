from __future__ import annotations


class PostMessage:
    def __init__(
            self,
            userId: int,
            id: int,
            title: str,
            body: str
    ) -> None:
        self.userId = userId
        self.id = id
        self.title = title
        self.body = body

    @classmethod
    def from_response_json(cls, data: dict) -> PostMessage:
        return cls(**data)

    def __eq__(self, other: PostMessage) -> bool:
        return self.userId == int(other.userId) and \
               self.id == int(other.id) and \
               self.title == other.title and \
               self.body == other.body

    def __str__(self) -> str:
        result = ''

        for key, value in self.__dict__.items():
            result += f'{key} => {value}\n'
        return result
