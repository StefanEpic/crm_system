import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_system.settings')

app = Celery('crm_system')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_everyday_8am': {
        'task': 'crm.tasks.change_of_date_everyday_8am',
        'schedule': crontab(minute=0, hour=8),
    },
}
