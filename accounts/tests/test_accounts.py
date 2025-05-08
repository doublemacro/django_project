import pytest
from django.contrib.auth import get_user_model
from accounts.models import UserLoginMetadata

@pytest.fixture
def user(db):
    return get_user_model().objects.create_user(username="adrian", password="tomatoes12345")


@pytest.mark.django_db
def test_create_user():
    user = get_user_model().objects.create_user(username="user1", password="password12345")
    assert user is not None
    assert user.username == "user1"
    user = get_user_model().objects.create_user(username="user2", password="password12345")
    assert len(get_user_model().objects.all()) == 2


def test_login_metadata_creation(user, client):
    client.login(username="adrian", password="tomatoes12345")
    metadata_list = UserLoginMetadata.objects.filter(user = user).all()
    assert len(metadata_list) == 1

    client.logout()
    client.login(username="adrian", password="tomatoes12345")
    metadata_list = UserLoginMetadata.objects.filter(user = user).all()
    assert len(metadata_list) == 2
