from django.http import HttpResponse
import logging
from models import Order, OrderItem
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta

# Create your views here.

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
    return render(request, 'orders.html', {'orders': orders})


def ordered_items_view(request, period):
    today = timezone.now()
    if period == 'week':
        start_date = today - timedelta(days=7)
    elif period == 'month':
        start_date = today - timedelta(days=30)
    elif period == 'year':
        start_date = today - timedelta(days=365)

    ordered_items = OrderItem.objects.filter(order__date_ordered__gte=start_date).distinct('product')

    return render(request, 'ordered_items.html', {'ordered_items': ordered_items, 'period': period})
