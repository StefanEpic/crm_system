import datetime
from celery import shared_task

from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string

from .models import Task


@shared_task
def send_notify_about_task(task, label):
    employees = [e.email for e in task.employee.all()]
    projects = ','.join([p.name for p in task.project.all()])

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


@shared_task
def change_of_date_everyday_8am():
    today = datetime.date.today()
    tasks = Task.objects.filter(end__lt=today)
    for task in tasks:
        task.end = today
        task.save(update_fields=['end'])
