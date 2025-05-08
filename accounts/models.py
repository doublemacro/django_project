from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserLoginMetadata(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="login_metadata")
    # login time, user_agent, ip address,
    login_time = models.DateTimeField()
    ip_address = models.CharField(max_length=255)
    user_agent = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'User {} last login {}, with IP {}, user agent: {}'.format(self.user.username, self.login_time, self.ip_address, self.user_agent)
