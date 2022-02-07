import pytest


@pytest.mark.post_message
def test_get_post_response_status_code(posts_service):
    assert posts_service.get_response_status_code() == 200


@pytest.mark.post_message
def test_get_first_post_message_response(posts_service, posts):
    assert posts == posts_service.get_post_message_by_id(1)


@pytest.mark.post_message
def test_add_new_post_check_response(posts_service, post_after_add):
    assert post_after_add == posts_service.add_new_post_message(title="New Post", body="Body", userId=25)


@pytest.mark.post_message
def test_updating_post_check_put_response(posts_service, post_after_update):
    assert post_after_update == posts_service.update_post_message(id=2, title="New Post", body="Body", userId=1)


@pytest.mark.post_message
def test_patching_post_check_patch_response(posts_service, post_after_patch):
    assert post_after_patch == posts_service.patch_post_message(id=2, title="Patch Post", body="Patch Body")


@pytest.mark.post_message
def test_deleting_post_check_delete_response_status_code(posts_service):
    assert posts_service.delete_post_message_status_code(id=1) == 200
