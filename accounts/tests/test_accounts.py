import pytest
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_create_user():
    user = get_user_model().objects.create_user(username="user1", password="password12345")
    assert user is not None
    assert user.username == "user1"
    user = get_user_model().objects.create_user(username="user2", password="password12345")
    assert len(get_user_model().objects.all()) == 2
