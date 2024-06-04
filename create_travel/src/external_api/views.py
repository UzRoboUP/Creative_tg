from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import requests
from .serializers import HotelSerializer, AirTicketSerializer
from .models import HotelSearch

from core.settings.base import HOTEL_API_URL, HOTEL_KEY_ID, HOTEL_KEY_TOKEN_TEST, HOTEL_API_DETAIL_URL


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
# HOTEL_KEY_TEST="43a33a2a-ca60-4d32-9394-03e7ed413572"
# HOTEL_API_URL="https://api.worldota.net/api/b2b/v3/search/serp/region/"
# HOTEL_KEY_ID="4930"


class HotelAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=HotelSerializer
    # permission_classes=[IsAuthenticated,]
    def post(self,request):
        serializer=HotelSerializer(request.data)
        # serializer.is_valid(raise_exception=True)
        try:
            hotel_search_response = requests.post(url=HOTEL_API_URL, auth=(HOTEL_KEY_ID,HOTEL_KEY_TOKEN_TEST), json=serializer.data)
            data = hotel_search_response.json()
            hotel_detail_list={}
            for hotel_id in range(len(data['data']['hotels'])):
                hotel=data['data']['hotels'][hotel_id]
                print(hotel)
                hotel_detail:dict={"id":hotel['id'], "language":request.data['language']}
                detail=requests.post(url=HOTEL_API_DETAIL_URL,auth=(HOTEL_KEY_ID,HOTEL_KEY_TOKEN_TEST), json=hotel_detail)   
                data['data']['hotels'][hotel_id]['hotel_detail']=detail.json()

            print(data)
            return Response(data=data)
        except Exception:
            raise Response(hotel_search_response.status_code)
        


class AirTicketAPIView(generics.GenericAPIView):
    queryset=None
    serializer_class=AirTicketSerializer
    
    def post(self, request):
        data=request.data
        return Response(data=data)
