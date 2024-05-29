from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import requests
from .serializers import HotelSerializer, AirTicketSerializer
from .models import HotelSearch

from core.settings.base import HOTEL_API_URL, HOTEL_KEY_ID, HOTEL_KEY_TOKEN


# data = {
#     "checkin": "2024-06-25",
#     "checkout": "2024-06-26",
#     # "residency": "ru",
#     "language": "en",
#     "guests": [
#         {
#             "adults": 3,
#             "children": [4,1,3]
#         }
#     ],
#     "region_id": 965849726,
#     "currency": "UZS"
# }

class HotelAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=HotelSerializer
    permission_classes=[IsAuthenticated,]
    def post(self,request):
        serializer=HotelSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        try:
            response = requests.post(url=HOTEL_API_URL, auth=(HOTEL_KEY_ID,HOTEL_KEY_TOKEN), json=serializer.data)
            data = response.json()
            return Response(data=data)
        except Exception:
            raise Response(data=response.status_code)
        

class AirTicketAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=AirTicketSerializer
    
    def post(self, request):
        data=request.data
        return Response(data=data)
