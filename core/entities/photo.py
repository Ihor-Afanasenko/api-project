from __future__ import annotations


class Photo:
    def __init__(
            self,
            albumId: int,
            id: int,
            title: str,
            url: str,
            thumbnailUrl: str
    ) -> None:
        self.albumId = albumId
        self.id = id
        self.title = title
        self.url = url
        self.thumbnailUrl = thumbnailUrl

    @classmethod
    def from_response_json(cls, data: dict) -> Photo:
        return cls(**data)

    def __eq__(self, other: Photo) -> bool:
        return self.albumId == int(other.albumId) and \
               self.id == int(other.id) and \
               self.title == other.title and \
               self.url == other.url and \
               self.thumbnailUrl == other.thumbnailUrl

    def __str__(self) -> str:
        result = ''

        for key, value in self.__dict__.items():
            result += f'{key} => {value}\n'
        return result
