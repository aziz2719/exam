from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField('Номер телефона', max_length=30)
    address = models.CharField('Адрес', max_length=100)
    image = models.ImageField('Аватарка', upload_to='user_avatar/')

    def __str__(self):
        return self.username