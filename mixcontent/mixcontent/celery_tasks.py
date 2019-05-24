"""
celery's tasks
"""
from __future__ import print_function
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mixcontent.settings')

app = Celery('mixcontent')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(var):
    """ sample task """
    print('Request: {0!r}'.format(var.request))
