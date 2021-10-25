
from django.db import models
from django.utils.translation import pgettext_lazy
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length= 255)
    crated_at = models.DateTimeField(default= datetime.now(),verbose_name="Fecha de creacion")
    updated_at = models.DateTimeField(default= datetime.now,verbose_name="Fecha de creacion")
    addres = models.CharField(max_length=500,unique=True,verbose_name=pgettext_lazy('Hotel','direccion'))

    def __str__(self):
        return self.name
    class Meta:
        # Define the database table
        db_table = 'hotel'
        ordering = ['id']
        verbose_name = pgettext_lazy('Hotel', 'Hotel')
        verbose_name_plural = pgettext_lazy('Hotel', 'Hotels')

class RoomType(models.Model):
    name = models.CharField(max_length=255,unique=True,verbose_name=pgettext_lazy('RoomType','name'))
    description = models.TextField(blank=True,verbose_name=pgettext_lazy('RoomType','description'))

    class Meta:
        # Define the database table
        db_table = 'hotels_roomtypes'
        ordering = ['id']
        verbose_name = pgettext_lazy('RoomType', 'Room type')
        verbose_name_plural = pgettext_lazy('RoomType', 'Room types')

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey('Hotel',on_delete=models.PROTECT,verbose_name=pgettext_lazy('Room','hotel'))
    name = models.CharField(max_length=255,verbose_name=pgettext_lazy('Room','name'))
    description = models.TextField(blank=True,verbose_name=pgettext_lazy('Room','description'))
    room_type = models.ForeignKey('RoomType',on_delete=models.PROTECT,verbose_name=pgettext_lazy('Room','room type'))
    phone1 = models.CharField(max_length=255,blank=True,verbose_name=pgettext_lazy('Room','phone 1'))
    seats_base = models.PositiveIntegerField(default=1,verbose_name=pgettext_lazy('Room','seats base'))
    seats_additional = models.PositiveIntegerField(default=0,verbose_name=pgettext_lazy('Room','seats additional'))
    booked = models.BooleanField(default=False,verbose_name=pgettext_lazy('Room','booked Room'))

    class Meta:
        # Define the database table
        db_table = 'hotels_rooms'
        ordering = ['hotel', 'id']
        verbose_name = pgettext_lazy('Room', 'Room')
        verbose_name_plural = pgettext_lazy('Room', 'Rooms')

    def __str__(self):
        return '{HOTEL} - {NAME}'.format(HOTEL=self.hotel.name, NAME=self.name)

class Booking(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.PROTECT, verbose_name=pgettext_lazy('Booking', 'hotel'))
    room = models.ForeignKey('Room', on_delete=models.PROTECT, verbose_name=pgettext_lazy('Booking', 'room'))
    user = models.IntegerField(default=0,verbose_name='user')
    class Meta:
        # Define the database table
        db_table = 'hotels_rooms_booking'
        ordering = ['room', 'id']
        verbose_name = pgettext_lazy('Booking', 'Booking')
        verbose_name_plural = pgettext_lazy('Booking', 'Bookings')



    def __str__(self):
        return '{USER} - {ROOM}'.format(USER=self.user.name, ROOM=self.room.name)
