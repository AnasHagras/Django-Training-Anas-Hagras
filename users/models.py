from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(max_length = 256, default= '')
    def __str__(self):
        return self.username