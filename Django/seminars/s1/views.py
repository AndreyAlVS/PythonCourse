from django.http import HttpResponse
from django.shortcuts import render
from random import choice, randint
import logging

logger = logging.getLogger(__name__)


# Create your views here.

def index(request):
    logger.info('Index page accessed')
    return HttpResponse('Wellcome to seminar 1 "Introduction to Django"')


def coin(request):
    result = choice(['орёл', 'решка', 'ребро'])
    if result == 'орёл' or 'решка':
        logger.info(f'На монетке выпал {result}')
        return HttpResponse(f'На монетке выпал {result}')
    else:
        logger.exception(f'Error, монетка встала на {result}')
        return HttpResponse(f'Монетка не может встать на {result}, перекиньте')



def cube(request):
    return HttpResponse(f'На кубике выпало число {randint(1, 6)}')


def number(request):
    return HttpResponse(f'Выпало число {randint(0, 100)}')
