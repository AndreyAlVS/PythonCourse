# Generated by Django 5.0.3 on 2024-03-31 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.CharField(max_length=100)),
                ('time_res', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
