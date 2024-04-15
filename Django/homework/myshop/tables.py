import django_tables2 as tables
from django.conf import settings
from myshop.models import Product


def render_photo(value):
    if value and hasattr(value, 'url'):
        return '<a href="{}" target="_blank"><img src="{}{}" style="max-width: 100px; max-height: 100px;"></a>'.format(
            value.url, settings.MEDIA_URL, value.url)
    else:
        return ''


class ProductTable(tables.Table):
    prod_name = tables.Column()
    description = tables.Column()
    price = tables.Column()
    quantity = tables.Column()
    photo = tables.Column(empty_values=())

    class Meta:
        model = Product
        template_name = "django_tables2/bootstrap4.html"
        fields = ("prod_name", "description", "price", "quantity", "photo")
