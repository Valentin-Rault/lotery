from django.shortcuts import render
from asgiref.sync import async_to_sync
import aiohttp
import asyncio


# Create your views here.
@asyncio.coroutine
async def getPrize(url, f=lambda x: x):
    async with aiohttp.ClientSession() as client_session:
        async with client_session.get(url) as client_response:
            data = await client_response.json()
            print(await client_response.text())
        return f(data)

def showRandomPrize(request):
    def make_upper(dic):
        dic['word'] = dic['word'].upper()
        return dic
    data = async_to_sync(getPrize)('http://localhost:8000/api/random-word', make_upper)
    return render(request, 'prize.html', data)
