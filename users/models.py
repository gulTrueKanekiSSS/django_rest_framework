from django.contrib.auth.models import AbstractUser
from django.db import models
from django_rest_framework.settings import NULLABLE
from materials.models import Course, Lesson


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


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_pay = models.DateField(auto_now_add=True, verbose_name='date_of_pay', **NULLABLE)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='оплаченный урок')
    sum_of_pay = models.IntegerField(verbose_name='сумма оплаты', **NULLABLE)
    way_of_pay = models.CharField(max_length=30, verbose_name='Способ оплаты', **NULLABLE)

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_subscribed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
