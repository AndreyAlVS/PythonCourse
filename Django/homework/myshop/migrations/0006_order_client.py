# Generated by Django 5.0.3 on 2024-04-12 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0005_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myshop.client'),
            preserve_default=False,
        ),
    ]
