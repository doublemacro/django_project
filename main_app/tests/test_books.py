import pytest
from django.contrib.auth import get_user_model
from main_app.models import Book

@pytest.mark.django_db
def test_create_book():
    user = get_user_model().objects.create_user(username="user1", password="password12345")
    book = Book.objects.create(title="Titlu1", author="Max Luther", page_count=3, created_by=user)

    assert book.title == "Titlu1"
    assert book.author == "Max Luther"
    assert book.created_by == user
