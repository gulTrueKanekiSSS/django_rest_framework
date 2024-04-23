from django.db import models
from django_rest_framework.settings import NULLABLE

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    preview = models.ImageField(upload_to="materials/previews/", **NULLABLE)
    description = (models.TextField())

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    preview = models.ImageField(upload_to="materials/previews/", **NULLABLE)
    video_url = models.CharField(max_length=150, verbose_name='Ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
