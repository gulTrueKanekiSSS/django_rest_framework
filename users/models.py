from django.contrib.auth.models import AbstractUser
from django.db import models
from django_rest_framework.settings import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email address', **NULLABLE)
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='phone number', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='city', **NULLABLE)
    avatar = models.ImageField(upload_to='avatars/', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

