# Generated by Django 3.2.8 on 2021-10-31 01:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelesCore', '0012_auto_20211030_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='begin_at',
            field=models.DateTimeField(default=datetime.date(2021, 10, 30), verbose_name='Fecha inicio reserva'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='crated_at',
            field=models.DateTimeField(default=datetime.date(2021, 10, 30), verbose_name='Fecha de creacion'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='ends_at',
            field=models.DateTimeField(default=datetime.date(2021, 10, 30), verbose_name='Fecha fin reserva'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='updated_at',
            field=models.DateTimeField(default=datetime.date(2021, 10, 30), verbose_name='Fecha de actualizacion'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='crated_at',
            field=models.DateTimeField(default=datetime.date(2021, 10, 30), verbose_name='Fecha de creacion'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='updated_at',
            field=models.DateTimeField(default=datetime.date(2021, 10, 30), verbose_name='Fecha de actualizacion'),
        ),
        migrations.AlterField(
            model_name='room',
            name='crated_at',
            field=models.DateTimeField(default=datetime.date(2021, 10, 30), verbose_name='Fecha de creacion'),
        ),
        migrations.AlterField(
            model_name='room',
            name='updated_at',
            field=models.DateTimeField(default=datetime.date(2021, 10, 30), verbose_name='Fecha de actualizacion'),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='crated_at',
            field=models.DateTimeField(default=datetime.date(2021, 10, 30), verbose_name='Fecha de creacion'),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='updated_at',
            field=models.DateTimeField(default=datetime.date(2021, 10, 30), verbose_name='Fecha de actualizacion'),
        ),
    ]