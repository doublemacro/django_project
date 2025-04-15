import pytest
from django.contrib.auth.models import User
from django.template.defaultfilters import title
from django.test.client import Client
from django.urls import reverse

from main_app.models import Book
from main_app.serializers import BookSerializer


@pytest.fixture
def user(db):
    return User.objects.create_user(username="adrian", password="tomatoes12345")


@pytest.fixture
def client_logged_in(client: Client, user):
    client.login(username="adrian", password="tomatoes12345")
    return client


@pytest.fixture
def book(user):
    return Book.objects.create(title="Test1", author="Test Author", page_count=300, created_by=user)


@pytest.fixture
def books(user):
    list1 = []
    list1.append(Book.objects.create(title="Test2", author="Test Author", page_count=301, created_by=user))
    list1.append(Book.objects.create(title="Test3", author="Test Author", page_count=302, created_by=user))
    return list1


def test_books_custom_view(client_logged_in, user, book, books):
    # testing "get" for all books
    response = client_logged_in.get("/custom_books/")
    assert response.status_code == 200
    assert response.data is not None
    assert len(response.data) == 3
    assert user is not None

    # testing "get" for just one book
    response_single_get = client_logged_in.get("/custom_books/1/")
    book_instance = response_single_get.data.serializer.instance
    # book_instance = BookSerializer(data=response_single_get.data)
    assert response_single_get.status_code == 200
    # assert book.title == book_instance.title
    # assert book.author == book_instance.author
    # assert book_instance.created_by == user
    assert book == book_instance

    response_single_get = client_logged_in.get("/custom_books/2/")
    book_instance = response_single_get.data.serializer.instance
    # book_instance = BookSerializer(data=response_single_get.data)
    assert response_single_get.status_code == 200
    assert books[0] == book_instance

    response_single_get = client_logged_in.get("/custom_books/3/")
    book_instance = response_single_get.data.serializer.instance
    # book_instance = BookSerializer(data=response_single_get.data)
    assert response_single_get.status_code == 200
    assert books[1] == book_instance

    response_get_wrong = client_logged_in.get("/custom_books/200/")
    assert response_get_wrong.status_code == 404
    assert "Book not found!" in response_get_wrong.content.decode()

    response_deleted = client_logged_in.delete("/custom_books/3/")
    assert response_deleted.status_code == 200
    assert "book deleted successfully!" in response_deleted.content.decode()

    # title = models.CharField(max_length=255)
    # author = models.CharField(max_length=255)
    # page_count = models.IntegerField()
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

    book_data_to_created = {
        "title": "Test Created 1",
        "author": "Test Creator 1",
        "page_count": 1,
        "created_by": user.id
    }
    response_created = client_logged_in.post("/custom_books/", book_data_to_created)
    assert response_created.status_code == 201
    assert Book.objects.filter(title="Test Created 1").exists()

    book_data_wrong = {
        "titlesjehfb": "Test Created 1",
        "sefsef": "Test Creator 1",
        "rrrg": 1,
        "created_by": user.id
    }
    response_errors = client_logged_in.post("/custom_books/", book_data_wrong)
    assert response_errors.status_code == 400


def test_my_books_view(client_logged_in, user, book, books):
    response = client_logged_in.get("/books/")
    decoded = response.content.decode()
    assert response.status_code == 200
    assert book.title in decoded
    assert books[0].title in decoded
    assert books[1].title in decoded

def test_add_book_view(client_logged_in, user, book, books):
    url = "/books/add/"
    # test GET request, should return .html page
    response = client_logged_in.get(url)
    decoded = response.content.decode()
    assert response.status_code == 200
    assert "Add a new book:" in decoded

    # template_list = [t.name for t in response.templates]
    template_list = []
    for t in response.templates:
        template_list.append(t.name)
    assert 'add_book.html' in template_list

    # test book creation, POST request.
    book_dict = {
        "title": "Book 3 Test",
        "author": "Creator 2 Test",
        "page_count": 2,
    }
    response = client_logged_in.post(url, book_dict)
    assert response.status_code == 200
    assert "Book added successfully!" in response.content.decode()

def test_confirm_delete(client_logged_in, user, book):
    url = "/books/confirm_delete/1/"
    response = client_logged_in.get(url)
    decoded = response.content.decode()
    assert response.status_code == 200
    assert "Are you sure you want to delete this book?" in decoded
    assert book.title in decoded

    assert len(Book.objects.all()) == 1
    response = client_logged_in.post("/books/delete/1/")
    assert response.status_code == 302
    assert len(Book.objects.all()) == 0

def test_get_all_users(db, client: Client):
    User.objects.create_user(username="adrian", password="tomatoes12345")
    User.objects.create_user(username="adrian2", password="tomatoes123452")

    url = "/users/"
    response = client.get(url)
    response = response.content.decode()
    assert "adrian" in response
    assert "adrian2" in response

def test_get_books_by_user(db, client: Client, books, user):
    user_id = user.id
    url = "/users/{}/books/".format(user_id)

    response = client.get(url)
    decoded = response.content.decode()

    assert str(books[0]) in decoded
    assert str(books[1]) in decoded

