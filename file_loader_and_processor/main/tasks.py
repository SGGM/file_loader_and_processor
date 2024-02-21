from celery import shared_task

from .models import File


@shared_task()
def task_execute(job_params):

    file = File.objects.get(pk=job_params["db_id"])

    file.processed = True

    file.save()
