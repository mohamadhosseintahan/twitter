import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    username = models.CharField(max_length=16, unique=True)

    email = models.EmailField(unique=True)

    name = models.CharField(max_length=16, blank=True, null=True)

    def __str__(self):
        return self.email
