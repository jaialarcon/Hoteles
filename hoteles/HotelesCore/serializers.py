from rest_framework import serializers

from HotelesCore.models import *

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id_hotel', 'name')

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ('id_room_type', 'name', 'description')

