from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['GET', 'POST'])
def HotelListView(request):
    if request.method == 'GET':
        model = Hotel.objects.all()
        serializer = HotelSerializer(model, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['GET'])
def RoomtypeListView(request, pk):
    if request.method == 'GET':
        try:
            model = RoomTypeSerializer.objects.filter(id_character=pk)
        except RoomTypeSerializer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RoomTypeSerializer(model, many=True)
        return Response(serializer.data)

