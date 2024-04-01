from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coin/', views.coin, name='coin'),
    path('cube/', views.cube, name='cube'),
    path('number/', views.number, name='number'),
    path('game/', views.game, name='game'),
    path('stat/', views.statistics, name='statistics'),
    path('authors/', views.create_authors, name='authors'),
]