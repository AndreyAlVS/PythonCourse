from django.urls import path
from myshop import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('orders/', views.orders_view, name='orders'),
    path('client_orders/<int:client_id>/', views.client_orders, name='client_orders'),
    path('product_table/', views.product_table, name='product_table'),
]