from django.db.models.signals import post_save
from django.dispatch import receiver
from main_app.models import Book, BookDetail
from main_app.utils import create_book_detail

# create a function that listens to a post_save signal, so that when a Book is created, we create a BookDetail entry in the db.

@receiver(post_save, sender=Book)
def listen_then_create_book_detail(sender, instance, created, **kwargs):
    if created:
        create_book_detail(instance)
