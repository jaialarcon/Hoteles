# Generated by Django 3.2.8 on 2021-10-30 05:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelesCore', '0008_auto_20211030_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='ends_at',
            field=models.DateTimeField(default=None, verbose_name='Fecha fin reserva'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='begin_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 0, 29, 10, 644140), verbose_name='Fecha inicio reserva'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='crated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 0, 29, 10, 644140), verbose_name='Fecha de creacion'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 0, 29, 10, 644140), verbose_name='Fecha de actualizacion'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='crated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 0, 29, 10, 643110), verbose_name='Fecha de creacion'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 0, 29, 10, 643110), verbose_name='Fecha de actualizacion'),
        ),
        migrations.AlterField(
            model_name='room',
            name='crated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 0, 29, 10, 643110), verbose_name='Fecha de creacion'),
        ),
        migrations.AlterField(
            model_name='room',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 0, 29, 10, 643110), verbose_name='Fecha de actualizacion'),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='crated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 0, 29, 10, 643110), verbose_name='Fecha de creacion'),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 0, 29, 10, 643110), verbose_name='Fecha de actualizacion'),
        ),
    ]