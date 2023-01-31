from django.shortcuts import render
import requests, time
import aiohttp
import asyncio

from .utils import fetch


# Ordinal View
def home_view(request):
    start_time = time.time()

    data = []
    url_list = ['https://swapi.dev/api/people/', 'https://swapi.dev/api/starships/']
    for url in url_list:
        data.append(requests.get(url).json())

    total = time.time() - start_time
    print(total)

    context = {
        'people': data[0],
        'starships':data[1],
    }

    return render(request, 'home.html', context)


# Async View
async def home_async(request):
    start_time = time.time()

    url_list = ['https://swapi.dev/api/people/', 'https://swapi.dev/api/starships/']
    async with aiohttp.ClientSession() as client:
        tasks =[]
        for url in url_list : 
            task = asyncio.ensure_future(fetch(client, url))
            tasks.append(task)
        results = await asyncio.gather(*tasks)

        total = time.time() - start_time
        print(total)

    context = {
        'people': results[0],
        'starships':results[1],
    }
    return render(request, 'home.html', context)
