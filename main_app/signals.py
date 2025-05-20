from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from main_app.models import Book, BookDetail
from main_app.utils import create_book_detail
import os

# create a function that listens to a post_save signal, so that when a Book is created, we create a BookDetail entry in the db.

@receiver(post_save, sender=Book)
def listen_then_create_book_detail(sender, instance, created, **kwargs):
    if created:
        create_book_detail(instance)

@receiver(pre_delete, sender=Book)
def delete_image_from_media(sender, instance, **kwargs):
    image_path = instance.image.path
    if os.path.exists(image_path):
        os.remove(image_path)
