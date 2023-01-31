from django.shortcuts import render, HttpResponse

from movies.models import Movie
from stories.models import Story

import time, asyncio

from asgiref.sync import sync_to_async

# Helper Functions
def get_movies():
    print('Prepare to get movies ...')
    time.sleep(3)
    movies = Movie.objects.all()
    print(movies)
    print('Done :)')


def get_stories():
    print('Prepare to get stories ...')
    time.sleep(4)
    stories = Story.objects.all()
    print(stories)
    print('Done :)')

# Async Helper Functions
@sync_to_async
def get_movies_async():
    print('Prepare to get movies ...')
    time.sleep(3)
    movies = Movie.objects.all()
    print(movies)
    print('Done :)')

@sync_to_async
def get_stories_async():
    print('Prepare to get stories ...')
    time.sleep(4)
    stories = Story.objects.all()
    print(stories)
    print('Done :)')



def home(request):
    stories = Story.objects.all()
    movies = Movie.objects.all()

    context = {
        'stories':stories,
        'movies':movies,
    }

    return render(request, 'home.html', context)


def sync_view(request):
    start_time = time.time()

    get_movies()
    get_stories()

    total = (time.time() - start_time)
    print('total :', total)
    return HttpResponse('sync')

# async await  ----- in this function, tasks process side by side
async def async_view(request):
    start_time = time.time()

    # task1 = asyncio.ensure_future(get_movies_async())
    # task2 = asyncio.ensure_future(get_stories_async())
    # await asyncio.wait([task1, task2])

    await asyncio.gather(get_movies_async(), get_stories_async())

    total = (time.time() - start_time)
    print('total :', total)
    return HttpResponse('sync')

