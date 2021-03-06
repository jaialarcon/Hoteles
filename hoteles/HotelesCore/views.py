
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from .models import *
from .serializers import *
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


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


@csrf_exempt
@api_view(['POST'])
def CheckInBooking(request):
    #hotel_id = request.data['hotel']
    #room = request.data['room']
    #user = request.data['user']
    #my_date = date(2021, 3, 2)

    begin_booking_date = request.data["begin_at"].split(" ")[0].split("-")
    year = int(begin_booking_date[0])
    month = int(begin_booking_date[1])
    day =  int(begin_booking_date[2])
    begin_date = datetime(year, month, day, 0, 0, 0, 0)
    end_booking_date = request.data["ends_at"].split(" ")[0].split("-")
    yearE = int(end_booking_date[0])
    monthE = int(end_booking_date[1])
    dayE = int(end_booking_date[2])
    end_date = datetime(yearE,monthE,dayE,0,0,0,0)
    hotel_id = request.data["id_hotel"]
    room = request.data["room"]
    user = request.data["user"]
    s_booking_room = {
        "data": {
            'message': 'Hotel does not exists'
        }

    }
    if request.method == 'POST':
        if Hotel.objects.filter(id_hotel=hotel_id).exists():
            if Room.objects.filter(id_room= room).exists():
                current_room = Room.objects.get(id_room= room)
                print("si hay habitaci??n")
                is_booked = current_room.booked
                print(is_booked)
                if not is_booked:
                    print("disponible")
                    #"print(request.data)
                    data ={
                            "hotel": hotel_id,
                            "room": room,
                            "user": user,
                            "begin_at": begin_date,
                            "ends_at": end_date,
                            "ends": False,
                    }
                    s_booking_room = BookingSerializer(data=data)
                    print(s_booking_room)
                    #print(s_booking_room.is_valid())
                    if s_booking_room.is_valid():
                        print(s_booking_room.is_valid())
                        print(s_booking_room)
                        print("VALIDO")
                        print("No est?? ocupada")
                        current_room.booked = True
                        current_room.save(force_update=True)
                        s_booking_room.save()
                        return Response(s_booking_room.data, status=status.HTTP_201_CREATED)


                else :
                    s_booking_room = {
                        'data':{
                            'message': 'Room is not available'
                        }

                    }
                    return Response(s_booking_room.get("data"), status=status.HTTP_404_NOT_FOUND)


        return Response(s_booking_room.data, status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['POST'])
def CheckOutBooking(request,pk):
    #hotel_id = request.data['hotel']
    #room = request.data['room']
    #user = request.data['user']
    #my_date = date(2021, 3, 2)
    begin_booking_date = request.data["begin_at"].split(" ")[0].split("-")
    year = int(begin_booking_date[0])
    month = int(begin_booking_date[1])
    day =  int(begin_booking_date[2])
    begin_date = datetime(year, month, day, 0, 0, 0, 0)
    end_booking_date = request.data["ends_at"].split(" ")[0].split("-")
    yearE = int(end_booking_date[0])
    monthE = int(end_booking_date[1])
    dayE = int(end_booking_date[2])
    end_date = datetime(yearE,monthE,dayE,0,0,0,0)
    hotel_id = request.data["id_hotel"]
    room = request.data["room"]
    user = request.data["user"]
    s_booking_room = {
        "data": {
            'message': 'Hotel does not exists'
        }

    }
    if request.method == 'POST':
        if Hotel.objects.filter(id_hotel=hotel_id).exists():
            if Room.objects.filter(id_room= room).exists():
                current_room = Room.objects.get(id_room= room)
                print("si hay habitaci??n")
                is_booked = current_room.booked
                print(is_booked)
                if not is_booked:
                    print("disponible")
                    #"print(request.data)
                    data ={
                            "hotel": hotel_id,
                            "room": room,
                            "user": user,
                            "begin_at": begin_date,
                            "ends_at": end_date,
                            "ends": False,
                    }
                    s_booking_room = BookingSerializer(data=data)
                    print(s_booking_room)
                    #print(s_booking_room.is_valid())
                    if s_booking_room.is_valid():
                        print(s_booking_room.is_valid())
                        print(s_booking_room)
                        print("VALIDO")
                        print("No est?? ocupada")
                        current_room.booked = True
                        current_room.save(force_update=True)
                        s_booking_room.save()
                        return Response(s_booking_room.data, status=status.HTTP_201_CREATED)


                else :
                    s_booking_room = {
                        'data':{
                            'message': 'Room is not available'
                        }

                    }
                    return Response(s_booking_room.get("data"), status=status.HTTP_404_NOT_FOUND)


        return Response(s_booking_room.data, status=status.HTTP_404_NOT_FOUND)
# @csrf_exempt
# @api_view(['PUT'])
# def CheckoutBooking(request):
#
#     booking_id = request.data['booking']
#     try:
#         begin_booking_date = request.data['begin_at']
#         parsed_begin_booking_date = datetime.date(begin_booking_date)
#     except:
#         print("Exception")
#
#     s_booking_room = {
#         "data" : {
#             'message': 'Hotel does not exists'
#         }
#
#     }
#     if request.method == 'PUT':
#         if Booking.objects.filter(id_booking=booking_id).exists():
#             booking_object = Booking.objects.get(id_booking = booking_id)
#             if Room.objects.filter(id_room=booking_object.room).exists():
#                 current_room = Room.objects.get(id_room=booking_object.room)
#
#                 is_booked = current_room.booked
#                 if is_booked:
#
#                     booking_object.ends = True
#                     current_room.booked = False
#                     current_room.save()
#                     booking_object.save()
#                     booking_data = {
#                         'ends': booking_object.ends
#                     }
#                     s_booking_room = Bookingerializer(data = booking_data)
#                     if s_booking_room.is_valid():
#                         s_booking_room.save()
#                     return Response(s_booking_room.data, status=status.HTTP_201_CREATED)
#                 else :
#                     s_booking_room = {
#                         'data':{
#                             'message': 'Room is not available'
#                         }
#
#                     }
#                     return Response(s_booking_room.data, status=status.HTTP_404_NOT_FOUND)
#
#
#         return Response(s_booking_room.data, status=status.HTTP_404_NOT_FOUND)@csrf_exempt
#
# @api_view(['PUT'])
# def CheckoutBooking(request):
#
#     booking_id = request.data['booking']
#     try:
#         begin_booking_date = request.data['begin_at']
#         parsed_begin_booking_date = datetime.date(begin_booking_date)
#     except:
#         print("Exception")
#
#     s_booking_room = {
#         "data" : {
#             'message': 'Hotel does not exists'
#         }
#
#     }
#     if request.method == 'PUT':
#         if Booking.objects.filter(id_booking=booking_id).exists():
#             booking_object = Booking.objects.get(id_booking = booking_id)
#             if Room.objects.filter(id_room=booking_object.room).exists():
#                 current_room = Room.objects.get(id_room=booking_object.room)
#
#                 is_booked = current_room.booked
#                 if is_booked:
#
#                     booking_object.ends = True
#                     current_room.booked = False
#                     current_room.save()
#                     booking_object.save()
#                     booking_data = {
#                         'ends': booking_object.ends
#                     }
#                     s_booking_room = Bookingerializer(data = booking_data)
#                     if s_booking_room.is_valid():
#                         s_booking_room.save()
#                     return Response(s_booking_room.data, status=status.HTTP_201_CREATED)
#                 else :
#                     s_booking_room = {
#                         'data':{
#                             'message': 'Room is not available'
#                         }
#
#                     }
#                     return Response(s_booking_room.data, status=status.HTTP_404_NOT_FOUND)
#
#
#         return Response(s_booking_room.data, status=status.HTTP_404_NOT_FOUND)
#
