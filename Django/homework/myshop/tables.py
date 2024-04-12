import django_tables2 as tables
from myshop.models import Product


class ProductTable(tables.Table):
    class Meta:
        model = Product
        template_name = "django_tables2/bootstrap.html"
        attrs = {'class': 'table table-striped'}
