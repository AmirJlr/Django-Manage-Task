from django.http import HttpResponse

from .tasks import task1



def home(request):

    task1.delay()
    return HttpResponse('Hello with the taste of the Celery')
    
