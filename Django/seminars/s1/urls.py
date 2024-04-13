from django.urls import path
from s1 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coin/<int:num>/', views.coin, name='coin'),
    path('cube/<int:num>/', views.cube, name='cube'),
    path('number/<int:num>/', views.number, name='number'),
    path('game/', views.game, name='game'),
    path('stat/', views.statistics, name='statistics'),
    path('authors/', views.create_authors, name='authors'),
    path('about/', views.about, name='about'),
    path('all_games/', views.all_games, name='all_games'),
    path('add_author/', views.add_author, name='add_author'),
]