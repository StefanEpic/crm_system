from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Task
from .tasks import send_notify_about_task


@receiver(post_save, sender=Task)
def notify_about_task(created, **kwargs):
    task = kwargs['instance']
    if created:
        label = 'Вам назначена новая задача'
    else:
        label = 'Внесены изменения в задачу'
    send_notify_about_task(task, label)
