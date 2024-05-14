from datetime import timedelta

from celery import shared_task
from django.utils import timezone
from django.core.mail import send_mail

from django_rest_framework import settings
from materials.models import Course
from users.models import User


@shared_task
def send_notice_courses_update(user_id):
    user = User.objects.filter(id=user_id).first()
    send_mail(
        subject='Ваш курс обновлен!',
        message='Курс обновлен, подробнее можете посмотреть в личном кабинете',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=True
    )

@shared_task
def check_updates():
    courses = Course.objects.all()
    now = timezone.now()
    for course in courses:
        lesson = courses.lesson_set.last()
        if lesson.date_create == now.date():
            for subscription in course.subscription_set.all():
                send_notice_courses_update.delay(subscription.user.id)

@shared_task
def check_last_login():
    now = timezone.now()

    users = User.objects.filter(is_active=True)

    for user in users:
        if user.last_login + timedelta(days=30) < now:
            user.is_active = False
            user.save()
