import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "file_loader_and_processor.settings")

app = Celery("file_loader_and_processor")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
