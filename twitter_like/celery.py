from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twitter_like.settings')

app = Celery('twitter_like')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Tehran')
app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks(related_name='tasks')


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
