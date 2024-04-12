from django.http import HttpResponse
import logging
from myshop.models import Order, OrderItem, Product, Client
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from myshop.tables import ProductTable

logger = logging.getLogger(__name__)


def home(request):
    html = (
        "<h1>Добро пожаловать в интернет магазин!</h1>"
        "<h2>Добро пожаловать в интернет магазин!</h2>"
        "<h3>Добро пожаловать в интернет магазин!</h3>"
    )
    log_data = f"Посещение главной страницы: {request.META.get('REMOTE_ADDR')} - {request.META.get('HTTP_USER_AGENT')}"
    logger.info(log_data)
    return HttpResponse(html)


def about(request):
    html = (
        "<h2>О магазине</h2>"
        "<h3>О магазине</h3>"
        "<p>Наш магазин действует с марта 2024 года</p>"
    )
    log_data = f"Посещение страницы 'О себе': {request.META.get('REMOTE_ADDR')} - {request.META.get('HTTP_USER_AGENT')}"
    logger.info(log_data)
    return HttpResponse(html)


def orders_view(request):
    orders = Order.objects.all()
    return render(request, 'myshop/orders.html', {'orders': orders})


def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    days_7_ago = timezone.now() - timedelta(days=7)
    days_30_ago = timezone.now() - timedelta(days=30)
    days_365_ago = timezone.now() - timedelta(days=365)
    orders = client.order_set.filter(date_ordered__gte=days_365_ago)
    return render(request, 'myshop/client_orders.html', {
        'client': client,
        'orders': orders,
        'days_7_ago': days_7_ago,
        'days_30_ago': days_30_ago,
        'days_365_ago': days_365_ago,
    })


def product_table(request):
    table = ProductTable(Product.objects.all())
    return render(request, 'myshop/product_table.html', {'table': table})
