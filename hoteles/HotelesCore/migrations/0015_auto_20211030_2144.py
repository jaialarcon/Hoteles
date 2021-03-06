# Generated by Django 3.2.8 on 2021-10-31 02:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelesCore', '0014_auto_20211030_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='begin_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 21, 44, 20, 64630)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='crated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 21, 44, 20, 64630)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 21, 44, 20, 64630)),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='crated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 21, 44, 20, 63630)),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 21, 44, 20, 63630)),
        ),
        migrations.AlterField(
            model_name='room',
            name='crated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 21, 44, 20, 63630)),
        ),
        migrations.AlterField(
            model_name='room',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 21, 44, 20, 63630)),
        ),
    ]
