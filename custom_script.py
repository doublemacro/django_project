import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from main_app.models import Book
from main_app.utils import create_book_detail

def run():

    books = Book.objects.all()
    for book in books:
        try:
            print(book.detail)
        except Exception as e:
            # book has no detail.
            create_book_detail(book)
            print("Created Book detail, for book:")
            print(book)


if __name__ == "__main__":
    run()
