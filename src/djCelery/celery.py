from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379')

# app.config_from_object('django.conf:settings', namespace = 'CELERY')


