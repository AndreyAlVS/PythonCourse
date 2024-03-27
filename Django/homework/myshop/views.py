from django.http import HttpResponse
import logging

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
