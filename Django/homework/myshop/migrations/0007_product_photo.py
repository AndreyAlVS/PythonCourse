# Generated by Django 5.0.3 on 2024-04-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0006_order_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(default=0, upload_to='product_photos/'),
            preserve_default=False,
        ),
    ]