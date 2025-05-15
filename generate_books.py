import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from main_app.models import Book
from main_app.utils import create_book_detail

def run():

    user = get_user_model().objects.get(pk=1)
    books = []
    for i in range(5000):
        # title = models.CharField(max_length=255)
        # author = models.CharField(max_length=255)
        # page_count = models.IntegerField()
        # created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

        books.append(Book(title=str(i * 3),
            author=str(i),
            page_count=300,
            created_by = user))

        if i % 1000 == 0:
            print(i)

    Book.objects.bulk_create(books)
    # Book.objects.all().delete()

if __name__ == "__main__":
    run()
