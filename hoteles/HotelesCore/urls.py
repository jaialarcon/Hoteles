from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path("hotels/",HotelListView),
    path('room_types/',RoomtypeListView),
]


