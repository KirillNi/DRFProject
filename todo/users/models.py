from django.db import models
from uuid import uuid4


class User(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4, verbose_name='uid')
    username = models.CharField(max_length=64, verbose_name='username')
    first_name = models.CharField(max_length=64, verbose_name='first name')
    last_name = models.CharField(max_length=64, verbose_name='last name')
    email = models.EmailField(unique=True, max_length=254, verbose_name='email address')
    birthday_year = models.PositiveIntegerField(verbose_name='birthday year')
