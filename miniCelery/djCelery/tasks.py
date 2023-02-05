from .celery import app
import time
from celery import shared_task


@app.task
def task1():
    time.sleep(8)
    open('task1.txt','w').close()


@shared_task
def add(x, y):
    return x + y
