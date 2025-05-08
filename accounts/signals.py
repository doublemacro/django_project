from ipaddress import ip_address

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.http import HttpRequest
from django.utils import timezone

from accounts.models import UserLoginMetadata

@receiver(user_logged_in)
def log_user_login(sender, request: HttpRequest, user, **kwargs):
    user_agent = request.META.get("HTTP_USER_AGENT", "")
    ip = request.META.get("REMOTE_ADDR")
    now = timezone.now()

    meta_data = UserLoginMetadata.objects.create(
        user=user,
        ip_address=ip,
        user_agent=user_agent,
        login_time=now
    )

