import os
# from __future__ import absolute_import, unicode_literals
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_rest_framework.settings')

app = Celery('django_rest_framework')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

