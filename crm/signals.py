from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.loader import render_to_string

from .models import Task


@receiver(post_save, sender=Task)
def notify_about_task(created, **kwargs):
    task = kwargs['instance']
    employees = [e.email for e in task.employee.all()]
    projects = ','.join([p.name for p in task.project.all()])
    if created:
        label = 'Вам назначена новая задача'
    else:
        label = 'Внесены изменения в задачу'

    html_content = render_to_string(
        'profile/email_notify.html',
        {
            'label': label,
            'name': task.name,
            'project': projects,
            'status': task.status,
            'end': task.end,
            'about': task.about,
        }
    )

    msg = EmailMultiAlternatives(
        subject=task.name,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=employees,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
