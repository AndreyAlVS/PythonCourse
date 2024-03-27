from  django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coin/', views.coin, name='coin'),
    path('cube/', views.cube, name='cube'),
    path('number/', views.number, name='number'),
]