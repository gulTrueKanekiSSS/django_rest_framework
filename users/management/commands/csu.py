from django.core.management import BaseCommand

from django_rest_framework.settings import admin_password
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@gmail.com',
            phone_number='+5555555555',
            first_name='Admin',
            last_name='gmail',
            is_staff=True,
            is_superuser=True
        )

        user.set_password(admin_password)
        user.save()