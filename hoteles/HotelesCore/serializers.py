from rest_framework import serializers

from HotelesCore.models import *

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id_graphic_designer', 'datetime')

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ('id_character', 'id_graphic_designer', 'name', 'datetime','url_image')

