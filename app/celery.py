from __future__ import absolute_import
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

from django.conf import settings

app = Celery('app')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
