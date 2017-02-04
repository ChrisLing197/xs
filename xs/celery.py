from __future__ import absolute_import

import os
import django
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ys.settings')
django.setup()

app=Celery('ys')

app.config_from_object('django.conf:settings')
#print(settings.INSTALLED_APPS)
# app.autodiscover_tasks(settings)
app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)

