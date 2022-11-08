from __future__ import absolute_import , unicode_literals
import os
from celery.schedules import crontab
from celery import Celery
import random 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicplatform.settings')
from datetime import timedelta , datetime
app = Celery('musicplatform')

app.conf.beat_schedule = {
    'add-every-day': {
        'task': 'artists.tasks.send_warning_messages',
        'schedule': timedelta(seconds=20),
    },
}


app.conf.enable_utc = False

app.conf.update(timezone = 'Europe/Istanbul')

app.config_from_object('django.conf:settings', namespace='CELERY_CONF')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')