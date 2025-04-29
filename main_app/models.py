from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    page_count = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return "{} by {}, {} pages.".format(self.title, self.author, self.page_count)


class BookDetail(models.Model):
    summary = models.TextField(blank=True)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13) # exemple: '9863583439450'
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name="detail")
