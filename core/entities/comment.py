from __future__ import annotations


class Comment:
    def __init__(
            self,
            postId: int,
            id: int,
            name: str,
            email: str,
            body: str
    ) -> None:
        self.postId = postId
        self.id = id
        self.name = name
        self.email = email
        self.body = body

    @classmethod
    def from_response_json(cls, data: dict) -> Comment:
        return cls(**data)

    def __eq__(self, other: Comment) -> bool:
        return self.postId == other.postId and \
               self.id == other.id and \
               self.name == other.name and \
               self.email == other.email and \
               self.body == other.body
