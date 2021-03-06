# Generated by Django 3.2.8 on 2021-10-30 05:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id_hotel', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('crated_at', models.DateTimeField(default=datetime.datetime(2021, 10, 30, 0, 25, 26, 247661), verbose_name='Fecha de creacion')),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2021, 10, 30, 0, 25, 26, 247661), verbose_name='Fecha de actualizacion')),
                ('address', models.CharField(max_length=500, unique=True, verbose_name='direccion')),
            ],
            options={
                'verbose_name': 'Hotel',
                'verbose_name_plural': 'Hotels',
                'db_table': 'hotel',
                'ordering': ['id_hotel'],
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id_room_type', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('crated_at', models.DateTimeField(default=datetime.datetime(2021, 10, 30, 0, 25, 26, 247661), verbose_name='Fecha de creacion')),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2021, 10, 30, 0, 25, 26, 248661), verbose_name='Fecha de actualizacion')),
            ],
            options={
                'verbose_name': 'Room type',
                'verbose_name_plural': 'Room types',
                'db_table': 'hotels_roomtypes',
                'ordering': ['id_room_type'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id_room', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('phone1', models.CharField(blank=True, max_length=255, verbose_name='phone 1')),
                ('seats_base', models.PositiveIntegerField(default=1, verbose_name='seats base')),
                ('seats_additional', models.PositiveIntegerField(default=0, verbose_name='seats additional')),
                ('booked', models.BooleanField(default=False, verbose_name='booked Room')),
                ('crated_at', models.DateTimeField(default=datetime.datetime(2021, 10, 30, 0, 25, 26, 248661), verbose_name='Fecha de creacion')),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2021, 10, 30, 0, 25, 26, 248661), verbose_name='Fecha de actualizacion')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='HotelesCore.hotel', verbose_name='id_hotel')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='HotelesCore.roomtype', verbose_name='id_room_type')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
                'db_table': 'hotels_rooms',
                'ordering': ['id_room'],
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id_booking', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.IntegerField(default=0, verbose_name='user')),
                ('crated_at', models.DateTimeField(default=datetime.datetime(2021, 10, 30, 0, 25, 26, 248661), verbose_name='Fecha de creacion')),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2021, 10, 30, 0, 25, 26, 248661), verbose_name='Fecha de actualizacion')),
                ('begin_at', models.DateTimeField(default=datetime.datetime(2021, 10, 30, 0, 25, 26, 248661), verbose_name='Fecha inicio reserva')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='HotelesCore.hotel', verbose_name='id_hotel')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='HotelesCore.room', verbose_name='room')),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
                'db_table': 'hotels_rooms_booking',
                'ordering': ['id_booking'],
            },
        ),
    ]
