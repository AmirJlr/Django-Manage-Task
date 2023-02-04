from django.http import HttpResponse
import time
from .celery import app



@app.task
def task1():
    time.sleep(8)
    open('task1.txt','w').close()



def home(request):

    task1.delay()
    return HttpResponse('Hello with the taste of the Celery')
