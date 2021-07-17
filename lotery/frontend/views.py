from django.shortcuts import render
import aiohttp
import asyncio

# Create your views here.

from aiohttp import web


@asyncio.coroutine
def getRandomPrize(request):
    return web.Response(text='Hello World')
