from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Account(models.Model):
    pass
