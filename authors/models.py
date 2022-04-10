from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

class MyUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name = 'возраст', default=18)
    phone = models.CharField(verbose_name='телефон', blank=True, max_length=20)
    city = models.CharField(verbose_name='город', blank=True, max_length=20)
    