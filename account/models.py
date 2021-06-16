from django.contrib.auth.models import AbstractUser
from django.db import models

from core import settings


class MyUser(AbstractUser):
    image = models.ImageField(upload_to='profile', blank=True, null=True,)
    username = models.CharField(max_length=70, unique=True)
    email = models.EmailField(unique=True)
    languages = list(settings.LANGUAGES)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    def __str__(self):
        return self.get_username()