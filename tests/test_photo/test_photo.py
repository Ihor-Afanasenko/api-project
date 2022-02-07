import pytest


@pytest.mark.photo
def test_get_photo_response_status_code(photo_service):
    assert photo_service.get_response_status_code() == 200


@pytest.mark.photo
def test_get_first_photo_response(photo_service, photo):
    assert photo == photo_service.get_photo_by_id(1)


@pytest.mark.photo
def test_add_new_photo_check_response(photo_service, photo_after_add):
    assert photo_after_add == photo_service.add_new_photo(albumId=1, title="Test Photo", url="https://test/url",
                                                          thumbnailUrl="https://test/thumbnalie")


@pytest.mark.photo
def test_put_new_photo_check_response(photo_service, photo_after_put):
    assert photo_after_put == photo_service.updating_photo(albumId=1, id=1, title="Test Photo", url="https://test/url",
                                                           thumbnailUrl="https://test/thumbnalie")


@pytest.mark.photo
def test_patch_new_photo_check_response(photo_service, photo_after_patch):
    assert photo_after_patch == photo_service.patch_photo(albumId=1, id=1, title="Test Photo", url="https://test/url")


@pytest.mark.photo
def test_deleting_post_check_delete_response_status_code(photo_service):
    assert photo_service.delete_photo_status_code(id=1) == 200
