# Generated by Django 5.0.3 on 2024-04-12 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0003_alter_order_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
    ]
