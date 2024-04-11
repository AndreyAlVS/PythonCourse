from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('orders/', views.orders_view, name='orders'),
    path('ordered_items/<str:period>/', views.ordered_items_view, name='ordered_items'),
]