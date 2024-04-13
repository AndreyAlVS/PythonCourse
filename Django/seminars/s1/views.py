from django.http import HttpResponse
from django.shortcuts import render, redirect
from random import choice, randint
import logging
from s1.models import Games, Author
import random
from s1.forms import GameForm, AuthorForm
from datetime import date

logger = logging.getLogger(__name__)


def index(request):
    context = {
        'title': 'index',
        'message': 'Its a index page',
    }
    logger.info('Index page accessed')
    # return HttpResponse('Wellcome to seminar 1 "Introduction to Django"')
    return render(request, 's1/index.html', context)


def about(request):
    context = {
        'title': 'About',
        'message': 'Its a about page',
    }
    return render(request, 's1/about.html', context)


def coin(request, num):
    result = [choice(['орёл', 'решка', 'ребро']) for _ in range(num)]
    context = {'result': result}
    # if result == 'орёл' or 'решка':
    #     logger.info(f'На монетке выпал {result}')
    #     return HttpResponse(f'На монетке выпал {result}')
    # else:
    #     logger.exception(f'Error, монетка встала на {result}')
    #     return HttpResponse(f'Монетка не может встать на {result}, перекиньте')
    return render(request, 's1/games.html', context)


def cube(request, num):
    result = [randint(1, 6) for _ in range(num)]
    context = {'result': result}
    return render(request, 's1/games.html', context)


def number(request, num):
    result = [randint(1, 100) for _ in range(num)]
    context = {'result': result}
    return render(request, 's1/games.html', context)


def game(request):
    side = random.choice(["orel", "reshka"])
    game = Games(side=side, )
    game.save()
    return HttpResponse(game)


def statistics(request):
    data = Games.stat_game()
    return HttpResponse(f'{data}')


def create_authors(request):
    result = []
    for i in range(10):
        author = Author(
            name=f'Name{i}',
            lastname=f'Lastname{i}',
            email=f'example{i}@mail.ru',
            biography=f'biography{i}',
            birthday=date.today()
        )
        author.save()
        result.append(author.fullname())
        return HttpResponse(f'{result}')


def all_games(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game_type = form.cleaned_data['game_type']
            num_tries = form.cleaned_data['num_tries']
            if game_type == 'coin':
                return redirect('coin', num_tries)
            elif game_type == 'cube':
                return redirect('cube', num_tries)
            else:
                return redirect('number', num_tries)
    else:
        form = GameForm()
    return render(request, 's1/all_games.html', {'form': form})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            biography = form.cleaned_data['biography']
            birthday = form.cleaned_data['birthday']
            author = Author(name=name, lastname=lastname, email=email, biography=biography, birthday=birthday)
            author.save()
            message = 'Author is added'
        else:
            message = 'uncorrected'
    else:
        form = AuthorForm()
        message = 'insert'
    return render(request, 's1/form.html', {'form': form, 'message': message})
