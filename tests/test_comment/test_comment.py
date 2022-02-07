import pytest


@pytest.mark.comment
def test_get_first_post_message_comment_with_second_id(posts_service, comment):
    assert comment == posts_service.get_post_message_comment_by_ids(1, 2)


@pytest.mark.comment
def test_get_second_post_message_comment_with_second_id(posts_service, second_comment):
    assert second_comment == posts_service.get_post_message_comment_by_id_and_position(2, 2)


@pytest.mark.comment
def test_get_first_post_message_comments_status_code(posts_service):
    assert posts_service.get_post_message_comments_status_code(3) == 200
