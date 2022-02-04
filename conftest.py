import pytest

from core import Config
from core import PostMessage, Comment, Photo
from services import PostsService, PhotoService


@pytest.fixture
def config():
    yield Config()


@pytest.fixture
def posts_service(config):
    yield PostsService(config)


@pytest.fixture
def photo_service(config):
    yield PhotoService(config)


@pytest.fixture
def posts() -> PostMessage:
    yield PostMessage.from_response_json(
        {
            "userId": 1,
            "id": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut"
                    " quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        }
    )


@pytest.fixture
def post_after_add() -> PostMessage:
    yield PostMessage.from_response_json(
        {
            "userId": 25,
            "id": 101,
            "title": "New Post",
            "body": "Body"
        }
    )


@pytest.fixture
def post_after_update() -> PostMessage:
    yield PostMessage.from_response_json(
        {
            "userId": 1,
            "id": 2,
            "title": "New Post",
            "body": "Body"
        }
    )


@pytest.fixture
def post_after_patch() -> PostMessage:
    yield PostMessage.from_response_json(
        {
            "userId": 1,
            "id": 2,
            "title": "Patch Post",
            "body": "Patch Body"
        }
    )


@pytest.fixture
def comment() -> Comment:
    yield Comment.from_response_json(
        {
            "postId": 1,
            "id": 2,
            "name": "quo vero reiciendis velit similique earum",
            "email": "Jayne_Kuhic@sydney.com",
            "body": "est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\n"
                    "voluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et"
        }
    )


@pytest.fixture
def photo() -> Photo:
    yield Photo.from_response_json(
        {
            "albumId": 1,
            "id": 1,
            "title": "accusamus beatae ad facilis cum similique qui sunt",
            "url": "https://via.placeholder.com/600/92c952",
            "thumbnailUrl": "https://via.placeholder.com/150/92c952"
        }
    )


@pytest.fixture
def photo_after_add() -> Photo:
    yield Photo.from_response_json(
        {
            "albumId": 1,
            "id": 5001,
            "title": "Test Photo",
            "url": "https://test/url",
            "thumbnailUrl": "https://test/thumbnalie"
        }
    )
